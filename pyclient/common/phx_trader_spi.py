from common.phx_protocol import *
from common.phx_structs import *


class CPhxFtdcTraderSpi(object):
    def __init__(self):
        pass

    # 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
    def OnFrontConnected(self):
        pass

    # 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
    # @param LinkType 0 Order 1 Qry 2 Rtn
    def OnFrontDisconnected(self, LinkType, nReason):
        print("OnFrontDisconnected, link=%d, nReason=%d" % (LinkType, nReason))

    # 心跳超时警告。当长时间未收到报文时，该方法被调用。
    # @param nTimeLapse 距离上次接收报文的时间
    def OnHeartBeatWarning(self, nTimeLapse):
        pass

    # 登录请求响应
    # @param LinkType 0 Order 1 Qry 2 Rtn
    def OnRspUserLogin(self, pRspUserLogin: CPhxFtdcRspUserLoginField, LinkType, ErrorID, nRequestID):
        pass

    # 登出请求响应
    def OnRspUserLogout(self, pUserLogout: CPhxFtdcRspUserLogoutField, LinkType, ErrorID, nRequestID):
        print('OnRspUserLogout, data=%s, ErrorID=%d, nRequestID=%d' % (json.dumps(pUserLogout.__dict__), ErrorID, nRequestID))

    # 报单录入请求响应
    def OnRspOrderInsert(self, pInputOrder: CPhxFtdcInputOrderField, ErrorID):
        pass

    # 报单操作请求响应
    def OnRspOrderAction(self, pInputOrderAction: CPhxFtdcOrderActionField, ErrorID):
        pass

    # 请求查询报单响应
    def OnRspQryOrder(self, pOrder: CPhxFtdcOrderField, ErrorID, nRequestID, bIsLast):
        print('OnRspQryOrder, data=%s, ErrorID=%d, bIsLast=%d' % (json.dumps(pOrder.__dict__), ErrorID, bIsLast))

    # 请求查询成交响应
    def OnRspQryTrade(self, pTrade: CPhxFtdcTradeField, ErrorID, nRequestID, bIsLast):
        print('OnRspQryTrade, data=%s, ErrorID=%d, bIsLast=%d' % (json.dumps(pTrade.__dict__), ErrorID, bIsLast))

    # 请求查询投资者持仓响应
    def OnRspQryInvestorPosition(self, pInvestorPosition: CPhxFtdcRspClientPositionField, ErrorID, nRequestID, bIsLast):
        print('OnRspQryInvestorPosition, data=%s, ErrorID=%d, bIsLast=%d' % (json.dumps(pInvestorPosition.__dict__), ErrorID, bIsLast))

    # 请求查询资金账户响应
    def OnRspQryTradingAccount(self, pTradingAccount: CPhxFtdcRspClientAccountField, ErrorID, nRequestID, bIsLast):
        print('OnRspQryTradingAccount, data=%s, ErrorID=%d, bIsLast=%d' % (json.dumps(pTradingAccount.__dict__), ErrorID, bIsLast))

    # 请求查询合约保证金率响应
    def OnRspQryInstrumentMarginRate(self, pInstrumentMarginRate: CPhxFtdcRspInstrumentMarginRateField, ErrorID, nRequestID, bIsLast):
        print('OnRspQryInstrumentMarginRate, data=%s, ErrorID=%d, bIsLast=%d' % (json.dumps(pInstrumentMarginRate.__dict__), ErrorID, bIsLast))

    # 请求查询合约手续费率响应
    def OnRspQryInstrumentCommissionRate(self, pInstrumentCommissionRate: CPhxFtdcRspInstrumentCommissionRateField, ErrorID, nRequestID, bIsLast):
        print('OnRspQryInstrumentCommissionRate, data=%s, ErrorID=%d, bIsLast=%d' % (json.dumps(pInstrumentCommissionRate.__dict__), ErrorID, bIsLast))

    # 请求查询合约响应
    def OnRspQryInstrument(self, pInstrument: CPhxFtdcRspInstrumentField, ErrorID, nRequestID, bIsLast):
        pass

    # 请求查询合约状态响应
    def OnRspQryInstrumentStatus(self, pInstrumentStatus: CPhxFtdcInstrumentStatusField, ErrorID, nRequestID, bIsLast):
        print('OnRspQryInstrumentStatus, data=%s, ErrorID=%d, bIsLast=%d' % (json.dumps(pInstrumentStatus.__dict__), ErrorID, bIsLast))

    # 增加合约通知
    def OnRtnInsInstrument(self, pInstrument: CPhxFtdcInstrumentField):
        print('OnRtnInsInstrument, data=%s' % json.dumps(pInstrument.__dict__))

    def OnRtnGameStatus(self, pGameStatus: CPhxFtdcGameStatusField):
        pass

    def OnRtnMarketData(self, pMarketData: CPhxFtdcDepthMarketDataField):
        pass

    # 报单通知
    def OnRtnOrder(self, pOrder: CPhxFtdcOrderField):
        pass

    # 成交通知
    def OnRtnTrade(self, pTrade: CPhxFtdcTradeField):
        pass

    # 报单录入错误回报
    def OnErrRtnOrderInsert(self, pInputOrder: CPhxFtdcInputOrderField, ErrorID):
        pass

    # 报单操作错误回报
    def OnErrRtnOrderAction(self, pOrderAction: CPhxFtdcOrderActionField, ErrorID):
        pass

    # 合约交易状态通知
    def OnRtnInstrumentStatus(self, pInstrumentStatus: CPhxFtdcInstrumentStatusField):
        print('OnRtnInstrumentStatus, data=%s' % json.dumps(pInstrumentStatus.__dict__))



