from common.phx_protocol import *
from common.phx_structs import *
from common.phx_definitions import *
from test.OrderList import OrderList, OrderInfo, Snapshot


class OrderManager(object):
    def __init__(self, instrument_id_):
        self.instrument_id = instrument_id_
        self.longSnapshot = Snapshot()
        self.shortSnapshot = Snapshot()
        self.longOpenPosition = 0
        self.shortOpenPosition = 0
        self.bid_list = OrderList(is_bid=True)
        self.ask_list = OrderList(is_bid=False)
        self.OrderRef2OrderInfo = {}
        self.snapshot = self.longSnapshot  # point to longSnapshot/shortSnapshot based on direction/offset
        self.order_list = self.bid_list  # point to bid_list/ask_list based on direction

    def place_limit_order(self, orderRef, direction, offset, price, volume):
        orderInfo = OrderInfo(orderRef=orderRef, priceType=PHX_FTDC_OPT_LimitPrice, direction=direction,
                              offset=offset, price=price, volume=volume, InstrumentID=self.instrument_id)
        return self._place_order(orderInfo)

    def place_market_order(self, orderRef, direction, offset, volume):
        orderInfo = OrderInfo(orderRef=orderRef, priceType=PHX_FTDC_OPT_AnyPrice, direction=direction,
                              offset=offset, volume=volume, InstrumentID=self.instrument_id)
        return self._place_order(orderInfo)

    def place_cancel_order(self, orderRef):
        if orderRef not in self.OrderRef2OrderInfo:
            return
        orderInfo = self.OrderRef2OrderInfo[orderRef]

        if OrderManager.is_tradable_status(orderInfo.OrderStatus):
            pass

    def on_rsp_order_insert(self, orderRef):
        if orderRef not in self.OrderRef2OrderInfo:
            return
        orderInfo = self.OrderRef2OrderInfo[orderRef]

        self.set_snapshot(orderInfo.Direction, orderInfo.OffsetFlag)
        self.set_order_list(orderInfo.Direction)
        old_status = orderInfo.OrderStatus
        orderInfo.OrderStatus = PHX_FTDC_OST_Error
        self.snapshot.TotalErrorTimes += 1

        tmp = orderInfo.VolumeTotalOriginal - orderInfo.VolumeTraded
        if old_status == PHX_FTDC_OST_Unknown:
            if orderInfo.OffsetFlag == PHX_FTDC_OF_Open:
                self.snapshot.OpenUnknownVolume -= tmp
            else:
                self.snapshot.FrozenPosition -= tmp
                self.snapshot.CloseUnknownVolume -= tmp
        else:
            if orderInfo.OffsetFlag == PHX_FTDC_OF_Open:
                self.snapshot.OpenUntradedVolume -= tmp
            else:
                self.snapshot.FrozenPosition -= tmp
                self.snapshot.CloseUntradedVolume -= tmp

        self.order_list.remove_by_order_ref(orderInfo.OrderLocalID)

    def on_rtn_order(self, order: CPhxFtdcOrderField):
        if order.OrderLocalID not in self.OrderRef2OrderInfo:
            return
        orderInfo = self.OrderRef2OrderInfo[order.OrderLocalID]

        if orderInfo.OrderSysID is None:
            orderInfo.OrderSysID = order.OrderSysID

        self.set_snapshot(orderInfo.Direction, orderInfo.OffsetFlag)
        self.set_order_list(orderInfo.Direction)

        if orderInfo.OrderStatus == PHX_FTDC_OST_Unknown and order.OrderStatus != PHX_FTDC_OST_Unknown:
            if orderInfo.OffsetFlag == PHX_FTDC_OF_Open:
                self.snapshot.OpenUnknownVolume -= order.VolumeTotalOriginal
                self.snapshot.OpenUntradedVolume += order.VolumeTotalOriginal
            else:
                self.snapshot.CloseUnknownVolume -= order.VolumeTotalOriginal
                self.snapshot.CloseUntradedVolume += order.VolumeTotalOriginal

        if order.OrderStatus == PHX_FTDC_OST_Canceled:
            self.snapshot.TotalCanceledTimes += 1

        orderInfo.OrderStatus = order.OrderStatus
        orderInfo.VolumeTraded = order.VolumeTraded

        if OrderManager.is_final_status(orderInfo.OrderStatus):
            tmp = orderInfo.VolumeTotalOriginal - orderInfo.VolumeTraded
            if orderInfo.OffsetFlag == PHX_FTDC_OF_Open:
                self.snapshot.OpenUntradedVolume -= tmp
            else:
                self.snapshot.FrozenPosition -= tmp
                self.snapshot.CloseUntradedVolume -= tmp

            self.order_list.remove_by_order_ref(orderInfo.OrderLocalID)
        # print('OnRtnOrder, data=%s' % json.dumps(order.__dict__))

    def on_rtn_trade(self, trade: CPhxFtdcTradeField):
        if trade.OrderLocalID not in self.OrderRef2OrderInfo:
            return

        orderInfo = self.OrderRef2OrderInfo[trade.OrderLocalID]
        orderInfo.TradeVolume += trade.Volume

        self.set_snapshot(orderInfo.Direction, orderInfo.OffsetFlag)

        if orderInfo.OffsetFlag == PHX_FTDC_OF_Open:
            self.snapshot.Position += trade.Volume
            self.snapshot.OpenVolume += trade.Volume
            self.snapshot.OpenUntradedVolume -= trade.Volume
        else:
            self.snapshot.Position -= trade.Volume
            self.snapshot.CloseVolume += trade.Volume
            self.snapshot.CloseUntradedVolume -= trade.Volume
        # print('OnRtnTrade, data=%s' % json.dumps(trade.__dict__))

    def get_total_canceled_times(self):
        return self.longSnapshot.TotalCanceledTimes + self.shortSnapshot.TotalCanceledTimes

    def get_total_error_times(self):
        return self.longSnapshot.TotalErrorTimes + self.shortSnapshot.TotalErrorTimes

    def get_total_order_times(self):
        return self.longSnapshot.TotalOrderTimes + self.shortSnapshot.TotalOrderTimes

    def get_open_volume(self):
        return self.longSnapshot.OpenVolume + self.shortSnapshot.OpenVolume

    def get_close_volume(self):
        return self.longSnapshot.CloseVolume + self.shortSnapshot.CloseVolume

    def get_traded_volume(self):
        return self.get_open_volume() + self.get_close_volume()

    def get_effective_long_trading_volume(self):
        return self.longSnapshot.OpenUnknownVolume + self.longSnapshot.OpenUntradedVolume \
               + self.shortSnapshot.CloseUnknownVolume + self.shortSnapshot.CloseUntradedVolume

    def get_effective_short_trading_volume(self):
        return self.shortSnapshot.OpenUnknownVolume + self.shortSnapshot.OpenUntradedVolume \
               + self.longSnapshot.CloseUnknownVolume + self.longSnapshot.CloseUntradedVolume

    def get_long_position_closeable(self):
        return self.longSnapshot.Position - self.longSnapshot.CloseUntradedVolume \
               - self.longSnapshot.CloseUnknownVolume

    def get_short_position_closeable(self):
        return self.shortSnapshot.Position - self.shortSnapshot.CloseUntradedVolume \
               - self.shortSnapshot.CloseUnknownVolume

    def get_effective_long_position(self):
        return self.longSnapshot.Position + self.get_effective_long_trading_volume()

    def get_effective_short_position(self):
        return self.shortSnapshot.Position + self.get_effective_short_trading_volume()

    def get_current_net_position(self):
        return self.get_effective_long_position() - self.get_effective_short_position()

    def get_current_net_holding_position(self):
        return self.longSnapshot.Position - self.shortSnapshot.Position

    def has_unknown_order(self):
        return self.longSnapshot.OpenUnknownVolume > 0 or self.longSnapshot.CloseUnknownVolume > 0 \
               or self.shortSnapshot.OpenUnknownVolume > 0 or self.shortSnapshot.CloseUnknownVolume > 0

    def get_unknown_orders(self):
        return self._get_orders_by(PHX_FTDC_OST_Unknown)

    def get_untraded_orders(self):
        return self._get_orders_by(PHX_FTDC_OST_NoTradeQueueing)

    def get_live_orders(self):
        bids = self.bid_list.get_orders()
        asks = self.ask_list.get_orders()
        return bids, asks

    def get_live_order_num(self):
        return self.bid_list.size() + self.ask_list.size()

    @staticmethod
    def is_final_status(status):
        return status == PHX_FTDC_OST_AllTraded or status == PHX_FTDC_OST_Canceled or status == PHX_FTDC_OST_Error

    @staticmethod
    def is_tradable_status(status):
        return status == PHX_FTDC_OST_PartTradedQueueing or status == PHX_FTDC_OST_NoTradeQueueing

    def clear(self):
        self.longSnapshot.clear()
        self.shortSnapshot.clear()
        self.bid_list.clear()
        self.ask_list.clear()
        self.longOpenPosition = 0
        self.shortOpenPosition = 0
        self.OrderRef2OrderInfo = {}

    def _get_orders_by(self, order_status):
        bids = self.bid_list.get_order_by_status(order_status)
        asks = self.ask_list.get_order_by_status(order_status)
        return bids, asks

    def _remove_order_from_list(self, orderInfo: OrderInfo):
        if orderInfo.OrderPriceType != PHX_FTDC_OPT_LimitPrice:
            return

        if orderInfo.Direction == PHX_FTDC_D_Buy:
            self.bid_list.remove_by_order_ref(orderInfo.OrderLocalID)
        else:
            self.ask_list.remove_by_order_ref(orderInfo.OrderLocalID)

    def _place_order(self, orderInfo: OrderInfo):
        self.OrderRef2OrderInfo[orderInfo.OrderLocalID] = orderInfo

        if orderInfo.Direction == PHX_FTDC_D_Buy:
            if orderInfo.OrderPriceType == PHX_FTDC_OPT_LimitPrice:
                self.bid_list.insert(orderInfo)
        else:
            if orderInfo.OrderPriceType == PHX_FTDC_OPT_LimitPrice:
                self.ask_list.insert(orderInfo)

        self.set_snapshot(orderInfo.Direction, orderInfo.OffsetFlag)
        self.snapshot.TotalOrderTimes += 1
        self.snapshot.TotalOrderVolume += orderInfo.VolumeTotalOriginal
        if orderInfo.OffsetFlag == PHX_FTDC_OF_Open:
            self.snapshot.OpenUnknownVolume += orderInfo.VolumeTotalOriginal
        else:
            self.snapshot.FrozenPosition += orderInfo.VolumeTotalOriginal
            self.snapshot.CloseUnknownVolume += orderInfo.VolumeTotalOriginal
        return orderInfo

    def set_order_list(self, direction):
        if direction == PHX_FTDC_D_Buy:
            self.order_list = self.bid_list
        else:
            self.order_list = self.ask_list

    def set_snapshot(self, direction, offset):
        if direction == PHX_FTDC_D_Buy:
            if offset == PHX_FTDC_OF_Open:
                self.snapshot = self.longSnapshot
            else:
                self.snapshot = self.shortSnapshot
        else:
            if offset == PHX_FTDC_OF_Open:
                self.snapshot = self.shortSnapshot
            else:
                self.snapshot = self.longSnapshot

    def insert_init_order(self, order: CPhxFtdcOrderField):
        if order.OrderLocalID in self.OrderRef2OrderInfo:
            return
        offset = PHX_FTDC_OF_Open
        if order.CombOffsetFlag[0] != PHX_FTDC_OF_Open:
            offset = PHX_FTDC_OF_Close

        if order.OrderPriceType == PHX_FTDC_OPT_AnyPrice:
            self.place_market_order(order.OrderLocalID, order.Direction, offset, order.VolumeTotalOriginal)
        else:
            self.place_limit_order(order.OrderLocalID, order.Direction, offset, order.LimitPrice, order.VolumeTotalOriginal)

