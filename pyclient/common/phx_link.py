from common.phx_protocol import *
from common.phx_structs import *
from common.phx_definitions import *
from common.phx_trader_spi import CPhxFtdcTraderSpi
import socket
import time


class PhxLink(object):
    def __init__(self, linkType):
        self.host = ''
        self.port = 0
        self.linkType = linkType
        self.socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.msg_left = b''
        self.msg_len = 0
        self.header = CPhxFtdcHeader()
        self.rsp_package = CPhxFtdcRspPackage()
        self.rsp_len = CPhxFtdcRspPackage.total_length()
        self.header_len = CPhxFtdcHeader.total_length()
        self.connected = False
        self.logined = False
        self.pSpi = None
        self.pApi = None
        self.last_reconnect_time = 0

    def RegisterSpi(self, spi_: CPhxFtdcTraderSpi):
        self.pSpi = spi_

    def RegisterApi(self, api):
        self.pApi = api

    def consume_server_data(self):
        while self.msg_len >= CPhxFtdcHeader.total_length():
            self.header.unpack(self.msg_left[0:CPhxFtdcHeader.total_length()])
            curr_msg_len = self.header.ContentLength + CPhxFtdcHeader.total_length()
            if self.msg_len >= curr_msg_len:
                # print("header", self.msg_len, curr_msg_len, self.header.Type, self.header.Chain, self.header.TransactionID)
                if self.header.Type == PHX_FTDC_TYPE_RSP:
                    self.rsp_package.unpack(self.msg_left[0:self.rsp_len])
                    if self.header.Chain == PHX_FTDC_CHAIN_SINGLE:
                        if self.rsp_package.TransactionID == PHX_FTDC_TID_RSP_LOGIN:
                            field = CPhxFtdcRspUserLoginField()
                            field.unpack(self.msg_left[self.rsp_len:self.rsp_len + CPhxFtdcRspUserLoginField.total_length()])
                            self.logined = True
                            self.pSpi.OnRspUserLogin(field, self.linkType, self.rsp_package.ErrorID, self.rsp_package.RequestID)
                        elif self.rsp_package.TransactionID == PHX_FTDC_TID_RSP_LOGOUT:
                            field = CPhxFtdcRspUserLogoutField()
                            field.unpack(self.msg_left[self.rsp_len:self.rsp_len + CPhxFtdcRspUserLogoutField.total_length()])
                            self.logined = False
                            self.pSpi.OnRspUserLogout(field, self.linkType, self.rsp_package.ErrorID, self.rsp_package.RequestID)
                        elif self.rsp_package.TransactionID == PHX_FTDC_TID_ERRRTN_ORDERINSERT:
                            self.handle_rtn_single_rsp(CPhxFtdcInputOrderField, "OnErrRtnOrderInsert")
                        elif self.rsp_package.TransactionID == PHX_FTDC_TID_ERRRTN_ORDERACTION:
                            self.handle_rtn_single_rsp(CPhxFtdcOrderActionField, "OnErrRtnOrderAction")
                        elif self.rsp_package.TransactionID == PHX_FTDC_TID_RSP_ORDERINSERT:
                            self.handle_rtn_single_rsp(CPhxFtdcInputOrderField, "OnRspOrderInsert")
                        elif self.rsp_package.TransactionID == PHX_FTDC_TID_RSP_ORDERACTION:
                            self.handle_rtn_single_rsp(CPhxFtdcOrderActionField, "OnRspOrderAction")
                        else:
                            print("unknown TransactionID", self.rsp_package.TransactionID)
                    else:  # multi_rsp
                        if self.rsp_package.TransactionID == PHX_FTDC_TID_RSP_QRY_INSTRUMENT:
                            self.handle_multi_rsp(curr_msg_len, CPhxFtdcRspInstrumentField, "OnRspQryInstrument")
                        elif self.rsp_package.TransactionID == PHX_FTDC_TID_RSP_QRY_CLIENTPOSITION:
                            self.handle_multi_rsp(curr_msg_len, CPhxFtdcRspClientPositionField, "OnRspQryInvestorPosition")
                        elif self.rsp_package.TransactionID == PHX_FTDC_TID_RSP_QRY_ORDER:
                            self.handle_multi_rsp(curr_msg_len, CPhxFtdcOrderField, "OnRspQryOrder")
                        elif self.rsp_package.TransactionID == PHX_FTDC_TID_RSP_QRY_TRADE:
                            self.handle_multi_rsp(curr_msg_len, CPhxFtdcTradeField, "OnRspQryTrade")
                        elif self.rsp_package.TransactionID == PHX_FTDC_TID_RSP_QRY_CLIENTACCOUNT:
                            self.handle_multi_rsp(curr_msg_len, CPhxFtdcRspClientAccountField, "OnRspQryTradingAccount")
                        elif self.rsp_package.TransactionID == PHX_FTDC_TID_RSP_QRY_INSTRUMENTMARGINRATE:
                            self.handle_multi_rsp(curr_msg_len, CPhxFtdcRspInstrumentMarginRateField, "OnRspQryInstrumentMarginRate")
                        elif self.rsp_package.TransactionID == PHX_FTDC_TID_RSP_QRY_INSTRUMENTCOMMISSIONRATE:
                            self.handle_multi_rsp(curr_msg_len, CPhxFtdcRspInstrumentCommissionRateField, "OnRspQryInstrumentCommissionRate")
                        elif self.rsp_package.TransactionID == PHX_FTDC_TID_RSP_QRY_INSTRUMENTSTATUS:
                            self.handle_multi_rsp(curr_msg_len, CPhxFtdcInstrumentStatusField, "OnRspQryInstrumentStatus")
                        else:
                            print("unknown rsp TransactionID", self.rsp_package.TransactionID)
                elif self.header.Type == PHX_FTDC_TYPE_PUSH:
                    if self.header.TransactionID == PHX_FTDC_TID_RTN_ORDER:
                        self.handle_push(CPhxFtdcOrderField, "OnRtnOrder")
                    elif self.header.TransactionID == PHX_FTDC_TID_RTN_TRADE:
                        self.handle_push(CPhxFtdcTradeField, "OnRtnTrade")
                    elif self.header.TransactionID == PHX_FTDC_TID_RTN_INSTRUMENT_STATUS:
                        self.handle_push(CPhxFtdcInstrumentStatusField, "OnRtnInstrumentStatus")
                    elif self.header.TransactionID == PHX_FTDC_TID_RTN_INSTRUMENT:
                        self.handle_push(CPhxFtdcInstrumentField, "OnRtnInsInstrument")
                    elif self.header.TransactionID == PHX_FTDC_TID_RTN_GAMESTATUS:
                        self.handle_push(CPhxFtdcGameStatusField, "OnRtnGameStatus")
                    elif self.header.TransactionID == PHX_FTDC_TID_RTN_DEPTHMARKETDATA:
                        self.handle_push(CPhxFtdcDepthMarketDataField, "OnRtnMarketData")
                    else:
                        print("unknown push TransactionID", self.header.TransactionID)
                self.msg_len -= curr_msg_len
                self.msg_left = self.msg_left[curr_msg_len:]
            else:
                # print("ContentLength not enough", self.msg_len, self.header.ContentLength)
                break

    def handle_rtn_single_rsp(self, TField, TCallback):
        field = TField()
        field.unpack(self.msg_left[self.rsp_len:self.rsp_len + TField.total_length()])
        getattr(self.pSpi, TCallback)(field, self.rsp_package.ErrorID)

    def handle_push(self, TField, TCallback):
        field = TField()
        field.unpack(self.msg_left[self.header_len:self.header_len + TField.total_length()])
        getattr(self.pSpi, TCallback)(field)

    def handle_multi_rsp(self, curr_msg_len, TField, TCallback):
        count = self.get_multi_rsp_count(curr_msg_len - self.rsp_len, TField.total_length())
        # print("total count ", count, curr_msg_len, self.rsp_len, TField.total_length())
        field = TField()
        if count == 0 and self.rsp_package.Chain == PHX_FTDC_CHAIN_LAST:
            getattr(self.pSpi, TCallback)(None, self.rsp_package.ErrorID, self.rsp_package.RequestID, True)
        else:
            for i in range(count):
                is_last = self.rsp_package.Chain == PHX_FTDC_CHAIN_LAST and i == count - 1
                offset = self.rsp_len + i * TField.total_length()
                field.unpack(self.msg_left[offset:offset + TField.total_length()])
                getattr(self.pSpi, TCallback)(field, self.rsp_package.ErrorID, self.rsp_package.RequestID, is_last)

    def get_multi_rsp_count(self, length, single_len):
        if length % single_len != 0:
            raise ValueError("incorrect multi rsp count %d %d" % (length, single_len))
        return length // single_len

    def connect(self):
        if self.connected:
            print("link %d already connected" % self.linkType)

        try:
            self.socket_.connect((self.host, self.port))
        except Exception as e:
            print("link %d connect server failed due to %s" % (self.linkType, str(e)))
        else:
            self.connected = True
        return self.connected

    def send(self, msg, nRequestID, transactionID):
        req = CPhxFtdcReqPackage()
        req.RequestID = nRequestID
        req.TransactionID = transactionID
        req.Version = PHX_CLIENT_FTD_PROTOCOL_VERSION
        req.Type = PHX_FTDC_TYPE_REQ
        req.Chain = PHX_FTDC_CHAIN_SINGLE
        req.ContentLength = msg.total_length() + req.total_length() - CPhxFtdcHeader.total_length()
        if (not self.socket_send(req.pack())) or (not self.socket_send(msg.pack())):
            print("link %d send error, trigger all connection shutdown")
            self.pApi.disconnect_all()
            return False
        return True

    def socket_send(self, binary):
        try:
            self.socket_.sendall(binary)
        except:
            print("connected False, link type %d" % self.linkType)
            return False
        return True

    def on_recv(self):
        try:
            msg = self.socket_.recv(1024)
            if msg:
                recv_len = len(msg)
                self.msg_left = self.msg_left + msg
                self.msg_len += recv_len
                return recv_len
            else:
                return 0
        except (ConnectionError, ConnectionResetError) as e:
            print("on_recv ret -1", e)
            return -1
        except Exception as e:
            print("on_recv ret 0", e)
            return 0

    def HasFrontRegistered(self):
        if self.host and self.port:
            return True
        return False

    def disconnect(self):
        if self.connected:
            self.socket_.shutdown(2)  # 0 = done receiving, 1 = done sending, 2 = both
            self.socket_.close()
            self.connected = False
            self.socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("link %d shutdown" % self.linkType)

