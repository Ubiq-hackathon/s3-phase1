#!/usr/bin/env /opt/anaconda3/bin/python3.5
# -*- coding: utf-8 -*-

PHX_CLIENT_FTD_PROTOCOL_VERSION = 49    # '1'

PHX_LINK_TYPE_Order = 0
PHX_LINK_TYPE_Qry = 1
PHX_LINK_TYPE_Rtn = 2
PHX_LINK_TYPE_MD = 3
TOTAL_LINK_COUNT = PHX_LINK_TYPE_MD + 1

# FTDC报文类型定义
PHX_FTDC_TYPE_REQ = 0    # 请求报文类型
PHX_FTDC_TYPE_RSP = 1    # 应答报文类型
PHX_FTDC_TYPE_PUSH = 2    # 推送报文类型
PHX_FTDC_TYPE_HEARTBEAT = 60    # 心跳报文类型

# FTDC报文链类型定义
PHX_FTDC_CHAIN_SINGLE = 83      # 'S' 报文链中只有单个报文
PHX_FTDC_CHAIN_FIRST = 70   # 'F' 报文链的第一个报文
PHX_FTDC_CHAIN_CENTER = 67    # 'C' 报文链的中间报文
PHX_FTDC_CHAIN_LAST = 76    # 'L' 报文链的最后一个报文

# 基础功能类
PHX_FTDC_TID_BASE_MIN = 1000
# 客户登录请求
PHX_FTDC_TID_REQ_LOGIN = 1001
# 客户登录请求应答
PHX_FTDC_TID_RSP_LOGIN = 1002
# 客户登出请求
PHX_FTDC_TID_REQ_LOGOUT = 1003
# 客户登出请求应答
PHX_FTDC_TID_RSP_LOGOUT = 1004
# 客户认证请求
PHX_FTDC_TID_REQ_AUTHENTICATE = 1005
# 客户认证请求应答
PHX_FTDC_TID_RSP_AUTHENTICATE = 1006

# 报单服务类
PHX_FTDC_TID_ORDER_MIN = 2000
# 报单录入请求
PHX_FTDC_TID_REQ_ORDERINSERT = 2001
# 报单录入错误回报（柜台验证失败）
PHX_FTDC_TID_RSP_ORDERINSERT = 2002
# 报单录入错误回报（交易所验证失败）
PHX_FTDC_TID_ERRRTN_ORDERINSERT = 2003
# 报单操作执行请求
PHX_FTDC_TID_REQ_ORDERACTION = 2004
# 报单操作错误回报（柜台验证失败）
PHX_FTDC_TID_RSP_ORDERACTION = 2005
# 报单操作错误回报（交易所验证失败）
PHX_FTDC_TID_ERRRTN_ORDERACTION = 2006
# 报单状态回报
PHX_FTDC_TID_RTN_ORDER = 2007
# 报单成交回报
PHX_FTDC_TID_RTN_TRADE = 2008
# 快捷报单录入请求
PHX_FTDC_TID_REQ_QUICK_ORDERINSERT = 2009
# 批量快捷报单录入请求
PHX_FTDC_TID_REQ_BATCH_QUICK_ORDERINSERT = 2010

# 查询请求类
PHX_FTDC_TID_QRY_MIN = 3000
# 资金查询请求
PHX_FTDC_TID_REQ_QRY_CLIENTACCOUNT = 3001
# 资金查询回报
PHX_FTDC_TID_RSP_QRY_CLIENTACCOUNT = 3002
# 持仓查询请求
PHX_FTDC_TID_REQ_QRY_CLIENTPOSITION = 3003
# 持仓查询回报
PHX_FTDC_TID_RSP_QRY_CLIENTPOSITION = 3004
# 报单查询请求
PHX_FTDC_TID_REQ_QRY_ORDER = 3005
# 报单查询回报
PHX_FTDC_TID_RSP_QRY_ORDER = 3006
# 成交查询请求
PHX_FTDC_TID_REQ_QRY_TRADE = 3007
# 成交查询回报
PHX_FTDC_TID_RSP_QRY_TRADE = 3008
# 合约查询请求
PHX_FTDC_TID_REQ_QRY_INSTRUMENT = 3009
# 合约查询回报
PHX_FTDC_TID_RSP_QRY_INSTRUMENT = 3010
# 合约保证金率查询请求
PHX_FTDC_TID_REQ_QRY_INSTRUMENTMARGINRATE = 3011
# 合约保证金率查询回报
PHX_FTDC_TID_RSP_QRY_INSTRUMENTMARGINRATE = 3012
# 合约手续费率查询请求
PHX_FTDC_TID_REQ_QRY_INSTRUMENTCOMMISSIONRATE = 3013
# 合约手续费率查询回报
PHX_FTDC_TID_RSP_QRY_INSTRUMENTCOMMISSIONRATE = 3014
# 合约价格查询请求
PHX_FTDC_TID_REQ_QRY_INSTRUMENTPRICE = 3015
# 合约价格查询回报
PHX_FTDC_TID_RSP_QRY_INSTRUMENTPRICE = 3016
# 合约状态查询请求
PHX_FTDC_TID_REQ_QRY_INSTRUMENTSTATUS = 3017
# 合约状态查询回报
PHX_FTDC_TID_RSP_QRY_INSTRUMENTSTATUS = 3018

# 操作员级别查询
# 投资者信息查询请求
PHX_FTDC_TID_REQ_QRY_INVESTORINFO = 3100
# 投资者信息查询回报
PHX_FTDC_TID_RSP_QRY_INVESTORINFO = 3101
# 报单查询请求扩展
PHX_FTDC_TID_REQ_QRY_ORDER_EX = 3102
# 报单查询回报扩展
PHX_FTDC_TID_RSP_QRY_ORDER_EX = 3103
# 成交查询请求扩展
PHX_FTDC_TID_REQ_QRY_TRADE_EX = 3104
# 成交查询回报扩展
PHX_FTDC_TID_RSP_QRY_TRADE_EX = 3105
# 系统状态查询请求
PHX_FTDC_TID_REQ_QRY_SYSTEMSTATUS = 3106
# 系统状态查询回报
PHX_FTDC_TID_RSP_QRY_SYSTEMSTATUS = 3107

# 推送类信息
PHX_FTDC_TID_RTN_MIN = 4000
# 新增合约信息推送
PHX_FTDC_TID_RTN_INSTRUMENT = 4001
# 合约状态信息推送
PHX_FTDC_TID_RTN_INSTRUMENT_STATUS = 4002
# 行情推送
PHX_FTDC_TID_RTN_DEPTHMARKETDATA = 4003
# 系统状态信息推送
PHX_FTDC_TID_RTN_SYSTEMSTATUS = 4004
# 比赛状态信息推送
PHX_FTDC_TID_RTN_GAMESTATUS = 4005

# 管理监控类信息
PHX_FTDC_TID_MANAGE_MIN = 5000
# 添加投资者
PHX_FTDC_TID_REQ_ADD_INVESTOR = 5001
# 添加投资者请求回报
PHX_FTDC_TID_RSP_ADD_INVESTOR = 5002
# 更新投资者信息请求
PHX_FTDC_TID_REQ_UPDATE_INVESTORINFO = 5003
# 更新投资者信息请求回报
PHX_FTDC_TID_RSP_UPDATE_INVESTORINFO = 5004

# client errors
PHXERR_CONN_FRONT_UNREACHABLE = 1000
PHXERR_CONN_FORCE_DISCONNECT = 1001
PHXERR_CONN_RTN_FRONT_UNREACHABLE = 1002
PHXERR_CONN_SEND_FAILED = 1003
PHXERR_CONN_QRY_FRONT_UNREGISTERED = 1004
PHXERR_CONN_RECV_FAILED = 1005
PHXERR_CONN_ALREADY_LOGIN = 1006
PHXERR_NO_USED_FOUND = 1007
PHXERR_NO_SPI_REGISTERED = 1100
PHXERR_NO_INTERNAL_ERROR = 1101
PHXERR_INVALID_PARAM = 1102
PHXERR_NOT_AUTHENTICATED = 1103

# server errors
SERVER_ERRORS = {
    0: "no error",
    101: "用户编码不存在",
    102: "投资者编码不存在",
    103: "用户密码错误",
    104: "指定的合约不存在",
    105: "指定订单系统编号不存在",
    106: "合约代码不存在",
    107: "订单数量超过单笔下单量上限",
    108: "订单数量小于单笔下单量下限",
    109: "订单价格超过合约价格上限",
    110: "订单价格低于合约价格下限",
    111: "下单价格类型不支持",
    112: "下单资金不足",
    113: "下单仓位不足",
    114: "不支持的投机套保类型",
    115: "不支持的开平仓标志",
    116: "不支持的买卖方向",
    117: "未授权操作",
    118: "该报单已撤消或已全部成交",
    119: "交易所报单错误",
    120: "交易所撤单错误",
    121: "内部数据查询错误",
    122: "请求参数不合法",
    123: "AppID不合法",
    124: "AuthCode错误",
    125: "用户已在另一个地方登录",
    126: "用户Token不存在",
    127: "用户被禁止开仓",
    128: "用户禁止交易",
    129: "非交易状态",
    130: "穿透认证厂商信息不一致",
    131: "穿透认证加密密钥版本不一致",
    132: "穿透认证加密失败",
    133: "穿透认证数据不合法",
    134: "订单本地编号非单调递增",
    135: "指定产品不存在",
    136: "比赛未开始或已结束",
    137: "该产品无交易权限",
    138: "外挂单数量超过最大限制",
    139: "单合约总订单数超过最大限制",
    140: "客户端请求速度超出限制"
}


def get_server_error(num):
    if num in SERVER_ERRORS:
        return SERVER_ERRORS[num]
    return "unknown server error"


