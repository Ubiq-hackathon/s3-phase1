import heapq
from common.phx_structs import *
import threading


class OrderInfo(object):
    def __init__(self, orderRef=0, priceType=PHX_FTDC_OPT_LimitPrice,
                 direction=PHX_FTDC_D_Buy, offset=PHX_FTDC_OF_Open, price=0, volume=0, InstrumentID=""):
        self.Direction = direction
        self.OffsetFlag = offset
        self.VolumeTotalOriginal = volume
        self.TradeVolume = 0  # update in trade event
        self.VolumeTraded = 0  # update in order event
        self.LimitPrice = price
        self.OrderLocalID = orderRef
        self.OrderSysID = None
        self.InstrumentID = InstrumentID
        self.OrderStatus = PHX_FTDC_OST_Unknown
        self.OrderPriceType = priceType

    def __str__(self):
        return json.dumps(self.__dict__)


class Snapshot(object):
    def __init__(self):
        self.Position = 0
        self.FrozenPosition = 0
        self.OpenUnknownVolume = 0
        self.OpenUntradedVolume = 0
        self.CloseUnknownVolume = 0
        self.CloseUntradedVolume = 0
        self.OpenVolume = 0
        self.CloseVolume = 0
        self.TotalOrderVolume = 0
        self.TotalOrderTimes = 0
        self.TotalCanceledTimes = 0
        self.TotalErrorTimes = 0

    def clear(self):
        self.Position = 0
        self.FrozenPosition = 0
        self.OpenUnknownVolume = 0
        self.OpenUntradedVolume = 0
        self.CloseUnknownVolume = 0
        self.CloseUntradedVolume = 0
        self.OpenVolume = 0
        self.CloseVolume = 0
        self.TotalOrderVolume = 0
        self.TotalOrderVolume = 0
        self.TotalOrderTimes = 0
        self.TotalCanceledTimes = 0
        self.TotalErrorTimes = 0

    def __str__(self):
        return json.dumps(self.__dict__)


class OrderList:
    def __init__(self, is_bid=True):
        self._value_lock = threading.Lock()
        self._queue = []
        self._index = 0
        self.priority_multiplier = 1
        if is_bid:
            self.priority_multiplier = -1

    def insert(self, order: OrderInfo):
        with self._value_lock:
            # _index helps the same priority follows FIFO
            heapq.heappush(self._queue, (self.priority_multiplier * order.LimitPrice, self._index, order))
        self._index += 1

    def get_best_order(self):
        with self._value_lock:
            if self.is_empty():
                return None
            return self._queue[0][-1]

    def remove(self):
        with self._value_lock:
            if self.is_empty():
                return None
            return heapq.heappop(self._queue)[-1]

    def remove_by_order_ref(self, orderRef):
        with self._value_lock:
            new_list = list(filter(lambda data: data[-1].OrderLocalID != orderRef, self._queue))
            if len(new_list) == self.size():
                return
            else:
                heapq.heapify(new_list)
                self._queue = new_list

    def size(self):
        return len(self._queue)

    def is_empty(self):
        return self.size() == 0

    def get_order_by_status(self, order_status):
        return [i[-1] for i in filter(lambda data: data[-1].OrderStatus == order_status, self._queue)]

    def get_orders(self):
        return [i[-1] for i in self._queue]

    def has_order_with_status(self, order_status):
        for data in self._queue:
            if data[-1].OrderStatus == order_status:
                return True
        return False

    def clear(self):
        self._queue = []
        self._index = 0


def insert_order(order_list, price, ref):
    order = OrderInfo()
    order.LimitPrice = price
    order.OrderLocalID = ref
    order_list.insert(order)


if __name__ == '__main__':
    bid_list = OrderList()
    insert_order(bid_list, 1.1, 1)
    insert_order(bid_list, 1.3, 2)
    insert_order(bid_list, 1.2, 3)
    print(bid_list.size())
    print(bid_list.get_best_order())
    print(len(bid_list.get_order_by_status(PHX_FTDC_OST_Unknown)))
    print(len(bid_list.get_order_by_status(PHX_FTDC_OST_AllTraded)))
    print(bid_list.has_order_with_status(PHX_FTDC_OST_Unknown))
    print(bid_list.has_order_with_status(PHX_FTDC_OST_AllTraded))
    print(bid_list.remove())
    print(bid_list.remove())
    print(bid_list.remove())

    ask_list = OrderList(False)
    insert_order(ask_list, 1.1, 1)
    insert_order(ask_list, 1.3, 2)
    insert_order(ask_list, 1.2, 3)
    print(ask_list.size())
    print(ask_list.get_best_order())
    print(len(ask_list.get_order_by_status(PHX_FTDC_OST_Unknown)))
    print(len(ask_list.get_order_by_status(PHX_FTDC_OST_AllTraded)))
    print(ask_list.has_order_with_status(PHX_FTDC_OST_Unknown))
    print(ask_list.has_order_with_status(PHX_FTDC_OST_AllTraded))
    print("size", ask_list.size())
    ask_list.remove_by_order_ref(3)
    print("size", ask_list.size())
    ask_list.remove_by_order_ref(3)
    print("size", ask_list.size())
    print(ask_list.remove())
    print(ask_list.remove())



