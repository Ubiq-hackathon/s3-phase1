from common.phx_protocol import *
from common.phx_structs import *
from common.phx_definitions import *
from common.phx_trader_spi import CPhxFtdcTraderSpi
import select
import threading
import time
from common.phx_link import PhxLink
import threading


class CPhxFtdcTraderApi(object):
    def __init__(self):
        self.pSpi = None
        self.orderLink = PhxLink(PHX_LINK_TYPE_Order)
        self.qryLink = PhxLink(PHX_LINK_TYPE_Qry)
        self.rtnLink = PhxLink(PHX_LINK_TYPE_Rtn)
        self.mdLink = PhxLink(PHX_LINK_TYPE_MD)
        self.inited = False
        self._is_started = False
        self._updater = threading.Thread(target=self.select_thread)
        self.good_links = {}
        self.all_connected = False
        self._lock = threading.Lock()

    # 初始化
    # @remark 初始化运行环境,只有调用后,接口才开始工作
    def Init(self):
        if self.inited:
            print("api already inited")
            return

        if not self.qryLink.HasFrontRegistered():
            self.pSpi.OnFrontDisconnected(self.qryLink.linkType, PHXERR_CONN_FRONT_UNREACHABLE)
        if not self.orderLink.HasFrontRegistered():
            self.pSpi.OnFrontDisconnected(self.orderLink.linkType, PHXERR_CONN_FRONT_UNREACHABLE)
        if not self.rtnLink.HasFrontRegistered():
            self.pSpi.OnFrontDisconnected(self.rtnLink.linkType, PHXERR_CONN_FRONT_UNREACHABLE)
        if not self.mdLink.HasFrontRegistered():
            self.pSpi.OnFrontDisconnected(self.mdLink.linkType, PHXERR_CONN_FRONT_UNREACHABLE)

        now = time.time()
        self.connect_link(self.qryLink, now)
        self.connect_link(self.orderLink, now)
        self.connect_link(self.rtnLink, now)
        self.connect_link(self.mdLink, now)

        self.start()
        self.inited = True
        self.all_connected = True
        if len(self.good_links) == TOTAL_LINK_COUNT:
            self.pSpi.OnFrontConnected()

    # 注册前置机网络地址
    def RegisterOrderFront(self, host, port):
        self.orderLink.host = host
        self.orderLink.port = port

    def RegisterQryFront(self, host, port):
        self.qryLink.host = host
        self.qryLink.port = port

    def RegisterRtnFront(self, host, port):
        self.rtnLink.host = host
        self.rtnLink.port = port

    def RegisterMDFront(self, host, port):
        self.mdLink.host = host
        self.mdLink.port = port

    # 注册回调接口
    # @param pSpi 派生自回调接口类的实例
    def RegisterSpi(self, spi_: CPhxFtdcTraderSpi):
        self.pSpi = spi_
        self.qryLink.RegisterSpi(spi_)
        self.rtnLink.RegisterSpi(spi_)
        self.orderLink.RegisterSpi(spi_)
        self.mdLink.RegisterSpi(spi_)
        self.qryLink.RegisterApi(self)
        self.rtnLink.RegisterApi(self)
        self.orderLink.RegisterApi(self)
        self.mdLink.RegisterApi(self)

    # 用户登录请求
    # @param LinkType 0 Order 1 Qry 2 Rtn
    def ReqUserLogin(self, pReqUserLoginField: CPhxFtdcReqUserLoginField, LinkType, nRequestID):
        if LinkType == PHX_LINK_TYPE_Order:
            return self.orderLink.send(pReqUserLoginField, nRequestID, PHX_FTDC_TID_REQ_LOGIN)
        elif LinkType == PHX_LINK_TYPE_Qry:
            return self.qryLink.send(pReqUserLoginField, nRequestID, PHX_FTDC_TID_REQ_LOGIN)
        elif LinkType == PHX_LINK_TYPE_Rtn:
            return self.rtnLink.send(pReqUserLoginField, nRequestID, PHX_FTDC_TID_REQ_LOGIN)
        elif LinkType == PHX_LINK_TYPE_MD:
            return self.mdLink.send(pReqUserLoginField, nRequestID, PHX_FTDC_TID_REQ_LOGIN)
        else:
            return False

    # 登出请求
    # @param LinkType 0 Order 1 Qry 2 Rtn
    def ReqUserLogout(self, pUserLogout: CPhxFtdcReqUserLogoutField, LinkType, nRequestID):
        if LinkType == PHX_LINK_TYPE_Order:
            return self.orderLink.send(pUserLogout, nRequestID, PHX_FTDC_TID_REQ_LOGOUT)
        elif LinkType == PHX_LINK_TYPE_Qry:
            return self.qryLink.send(pUserLogout, nRequestID, PHX_FTDC_TID_REQ_LOGOUT)
        elif LinkType == PHX_LINK_TYPE_Rtn:
            return self.rtnLink.send(pUserLogout, nRequestID, PHX_FTDC_TID_REQ_LOGOUT)
        elif LinkType == PHX_LINK_TYPE_MD:
            return self.mdLink.send(pUserLogout, nRequestID, PHX_FTDC_TID_REQ_LOGOUT)
        else:
            return False

    # 报单录入请求
    def ReqQuickOrderInsert(self, pInputOrder: CPhxFtdcQuickInputOrderField, nRequestID):
        return self.orderLink.send(pInputOrder, nRequestID, PHX_FTDC_TID_REQ_QUICK_ORDERINSERT)

    # 报单操作请求
    def ReqOrderAction(self, pInputOrderAction: CPhxFtdcOrderActionField, nRequestID):
        return self.orderLink.send(pInputOrderAction, nRequestID, PHX_FTDC_TID_REQ_ORDERACTION)

    # 请求查询报单
    def ReqQryOrder(self, pQryOrder: CPhxFtdcQryOrderField, nRequestID):
        return self.qryLink.send(pQryOrder, nRequestID, PHX_FTDC_TID_REQ_QRY_ORDER)

    # 请求查询成交
    def ReqQryTrade(self, pQryTrade: CPhxFtdcQryTradeField, nRequestID):
        return self.qryLink.send(pQryTrade, nRequestID, PHX_FTDC_TID_REQ_QRY_TRADE)

    # 请求查询投资者持仓
    def ReqQryInvestorPosition(self, pQryInvestorPosition: CPhxFtdcQryClientPositionField, nRequestID):
        return self.qryLink.send(pQryInvestorPosition, nRequestID, PHX_FTDC_TID_REQ_QRY_CLIENTPOSITION)

    # 请求查询资金账户
    def ReqQryTradingAccount(self, pQryTradingAccount: CPhxFtdcQryClientAccountField, nRequestID):
        return self.qryLink.send(pQryTradingAccount, nRequestID, PHX_FTDC_TID_REQ_QRY_CLIENTACCOUNT)

    # 请求查询合约保证金率
    def ReqQryInstrumentMarginRate(self, pQryInstrumentMarginRate: CPhxFtdcQryInstrumentMarginRateField, nRequestID):
        return self.qryLink.send(pQryInstrumentMarginRate, nRequestID, PHX_FTDC_TID_REQ_QRY_INSTRUMENTMARGINRATE)

    # 请求查询合约手续费率
    def ReqQryInstrumentCommissionRate(self, pQryInstrumentCommissionRate: CPhxFtdcQryInstrumentCommissionRateField, nRequestID):
        return self.qryLink.send(pQryInstrumentCommissionRate, nRequestID, PHX_FTDC_TID_REQ_QRY_INSTRUMENTCOMMISSIONRATE)

    # 请求查询合约
    def ReqQryInstrument(self, pQryInstrument: CPhxFtdcQryInstrumentField, nRequestID):
        return self.qryLink.send(pQryInstrument, nRequestID, PHX_FTDC_TID_REQ_QRY_INSTRUMENT)

    # 请求查询合约状态
    def ReqQryInstrumentStatus(self, pQryInstrumentStatus: CPhxFtdcQryInstrumentStatusField, nRequestID):
        return self.qryLink.send(pQryInstrumentStatus, nRequestID, PHX_FTDC_TID_REQ_QRY_INSTRUMENTSTATUS)

    def fetch_link(self, sock):
        if sock == self.qryLink.socket_:
            return self.qryLink
        elif sock == self.orderLink.socket_:
            return self.orderLink
        elif sock == self.rtnLink.socket_:
            return self.rtnLink
        elif sock == self.mdLink.socket_:
            return self.mdLink
        else:
            return None

    def on_data_in(self, sock):
        link = self.fetch_link(sock)
        if link is None:
            return

        ret = link.on_recv()
        if ret == 0:
            return
        elif ret < 0:
            self.disconnect_all()
        else:
            link.consume_server_data()

    def select_thread(self):
        while True:
            if len(self.good_links) < TOTAL_LINK_COUNT:
                self.try_reconnect()

            r_list = self.good_links.values()
            if len(r_list) > 0:
                rl, wl, error = select.select(r_list, [], [], 1)
                for sock in rl:
                    self.on_data_in(sock)
            else:
                time.sleep(1)

    def connect_link(self, link, now):
        if not link.connected and now - link.last_reconnect_time > 5:
            link.last_reconnect_time = now
            if not link.connect():
                self.pSpi.OnFrontDisconnected(link.linkType, PHXERR_CONN_FRONT_UNREACHABLE)
            else:
                self.good_links[link.linkType] = link.socket_
                print('connect (%s:%d) success' % (link.host, link.port))

    def disconnect_all(self):
        """if one link sense disconnect, disconnect all, because rtn link don't actively write,
        if disconnect happen, it cannot sense"""
        with self._lock:
            if self.all_connected:
                self.all_connected = False
                self.orderLink.disconnect()
                self.qryLink.disconnect()
                self.rtnLink.disconnect()
                self.mdLink.disconnect()
                self.pSpi.OnFrontDisconnected(PHX_LINK_TYPE_Order, PHXERR_CONN_FRONT_UNREACHABLE)
                self.pSpi.OnFrontDisconnected(PHX_LINK_TYPE_Qry, PHXERR_CONN_FRONT_UNREACHABLE)
                self.pSpi.OnFrontDisconnected(PHX_LINK_TYPE_Rtn, PHXERR_CONN_FRONT_UNREACHABLE)
                self.pSpi.OnFrontDisconnected(PHX_LINK_TYPE_MD, PHXERR_CONN_FRONT_UNREACHABLE)
                self.good_links = {}

    def try_reconnect(self):
        now = time.time()
        self.connect_link(self.qryLink, now)
        self.connect_link(self.orderLink, now)
        self.connect_link(self.rtnLink, now)
        self.connect_link(self.mdLink, now)

        if len(self.good_links) == TOTAL_LINK_COUNT:
            self.all_connected = True
            self.pSpi.OnFrontConnected()

    def start(self):
        if self._is_started:
            raise NotImplementedError

        self._is_started = True
        self._updater.start()

    def stop(self):
        if not self._is_started:
            raise NotImplementedError
        self._is_started = False



