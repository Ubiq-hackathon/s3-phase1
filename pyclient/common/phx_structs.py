import struct
import json


# 对话流
PHX_TSS_DIALOG = 1
# 会员私有流
PHX_TSS_PRIVATE = 2
# 公共流
PHX_TSS_PUBLIC = 3
# 查询
PHX_TSS_QUERY = 4
# 交易员私有流
PHX_TSS_USER = 5
# 询价流
PHX_TSS_FORQUOTE = 6

# 无效的交易所
PHX_FTDC_ED_NULL = 0
# 上海期货交易所
PHX_FTDC_ED_SHFE = 1
# 上海国际能源交易中心股份有限公司
PHX_FTDC_ED_INE = 2
# 大连商品交易所
PHX_FTDC_ED_DCE = 3
# 郑州商品交易所
PHX_FTDC_ED_CZCE = 4
# 中国金融交易所
PHX_FTDC_ED_CFFEX = 5

# 代理
PHX_FTDC_ER_Broker = '1'
# 自营
PHX_FTDC_ER_Host = '2'
# 做市商
PHX_FTDC_ER_MarketMaker = '3'

# 普通用户（可能包含机器人或者其他非参赛者）
PHX_FTDC_UT_USER = '0'
# 选手
PHX_FTDC_UT_PLAYER = '1'
# 操作员（普通）
PHX_FTDC_UT_OPERATOR = '2'
# 操作员（管理员)
PHX_FTDC_UT_OPERATOR_MANAGER = '3'

# 期货
PHX_FTDC_PC_Futures = '1'
# 期权
PHX_FTDC_PC_Option = '2'
# 组合
PHX_FTDC_PC_Combination = '3'
# 即期
PHX_FTDC_PC_Spot = '4'
# 期转现
PHX_FTDC_PC_EFP = '5'

# 非期权
PHX_FTDC_OT_NotOptions = '0'
# 看涨
PHX_FTDC_OT_CallOptions = '1'
# 看跌
PHX_FTDC_OT_PutOptions = '2'

# 开盘前
PHX_FTDC_IS_BeforeTrading = '0'
# 非交易
PHX_FTDC_IS_NoTrading = '1'
# 连续交易
PHX_FTDC_IS_Continous = '2'
# 集合竞价报单
PHX_FTDC_IS_AuctionOrdering = '3'
# 集合竞价价格平衡
PHX_FTDC_IS_AuctionBalance = '4'
# 集合竞价撮合
PHX_FTDC_IS_AuctionMatch = '5'
# 收盘
PHX_FTDC_IS_Closed = '6'

# 买
PHX_FTDC_D_Buy = '0'
# 卖
PHX_FTDC_D_Sell = '1'

# 净持仓
PHX_FTDC_PT_Net = '1'
# 综合持仓
PHX_FTDC_PT_Gross = '2'

# 多头
PHX_FTDC_PD_Long = '0'
# 空头
PHX_FTDC_PD_Short = '1'
# 净
PHX_FTDC_PD_Net = '2'

# 投机
PHX_FTDC_HF_Speculation = '1'
# 套利
PHX_FTDC_HF_Arbitrage = '2'
# 套保
PHX_FTDC_HF_Hedge = '3'

# 自然人
PHX_FTDC_CT_Person = '0'
# 法人
PHX_FTDC_CT_Company = '1'
# 投资基金
PHX_FTDC_CT_Fund = '2'

# 自动切换
PHX_FTDC_IER_Automatic = '1'
# 手动切换
PHX_FTDC_IER_Manual = '2'
# 熔断
PHX_FTDC_IER_Fuse = '3'
# 熔断手动
PHX_FTDC_IER_FuseManual = '4'

# 任意价
PHX_FTDC_OPT_AnyPrice = '1'
# 限价
PHX_FTDC_OPT_LimitPrice = '2'
# 最优价
PHX_FTDC_OPT_BestPrice = '3'
# 5档价
PHX_FTDC_OPT_FiveLevelPrice = '4'

# 开仓
PHX_FTDC_OF_Open = '0'
# 平仓
PHX_FTDC_OF_Close = '1'
# 强平
PHX_FTDC_OF_ForceClose = '2'
# 平今
PHX_FTDC_OF_CloseToday = '3'

# 非强平
PHX_FTDC_FCC_NotForceClose = '0'
# 资金不足
PHX_FTDC_FCC_LackDeposit = '1'
# 客户超仓
PHX_FTDC_FCC_ClientOverPositionLimit = '2'
# 会员超仓
PHX_FTDC_FCC_MemberOverPositionLimit = '3'
# 持仓非整数倍
PHX_FTDC_FCC_NotMultiple = '4'
# 违规
PHX_FTDC_FCC_Violation = '5'
# 其它
PHX_FTDC_FCC_Other = '6'
# 自然人临近交割
PHX_FTDC_FCC_PersonDeliv = '7'

# 全部成交
PHX_FTDC_OST_AllTraded = '0'
# 部分成交还在队列中
PHX_FTDC_OST_PartTradedQueueing = '1'
# 部分成交不在队列中
PHX_FTDC_OST_PartTradedNotQueueing = '2'
# 未成交还在队列中
PHX_FTDC_OST_NoTradeQueueing = '3'
# 未成交不在队列中
PHX_FTDC_OST_NoTradeNotQueueing = '4'
# 撤单
PHX_FTDC_OST_Canceled = '5'
# 未知
PHX_FTDC_OST_Unknown = '6'
# 错单
PHX_FTDC_OST_Error = '7'

# 正常
PHX_FTDC_ORDT_Normal = '0'
# 报价衍生
PHX_FTDC_ORDT_DeriveFromQuote = '1'
# 组合衍生
PHX_FTDC_ORDT_DeriveFromCombination = '2'

# 一方输入
PHX_FTDC_OOS_Inputed = '0'
# 已经确认
PHX_FTDC_OOS_Confirmed = '1'
# 已经撤销
PHX_FTDC_OOS_Canceled = '2'
# 已经拒绝
PHX_FTDC_OOS_Refused = '3'

# 立即完成，否则撤销
PHX_FTDC_TC_IOC = '1'
# 本节有效
PHX_FTDC_TC_GFS = '2'
# 当日有效
PHX_FTDC_TC_GFD = '3'
# 指定日期前有效
PHX_FTDC_TC_GTD = '4'
# 撤销前有效
PHX_FTDC_TC_GTC = '5'
# 集合竞价有效
PHX_FTDC_TC_GFA = '6'

# 任何数量
PHX_FTDC_VC_AV = '1'
# 最小数量
PHX_FTDC_VC_MV = '2'
# 全部数量
PHX_FTDC_VC_CV = '3'

# 立即
PHX_FTDC_CC_Immediately = '1'
# 止损
PHX_FTDC_CC_Touch = '2'

# 删除
PHX_FTDC_AF_Delete = '0'
# 挂起
PHX_FTDC_AF_Suspend = '1'
# 激活
PHX_FTDC_AF_Active = '2'
# 修改
PHX_FTDC_AF_Modify = '3'

# 来自参与者
PHX_FTDC_OSRC_Participant = '0'
# 来自管理员
PHX_FTDC_OSRC_Administrator = '1'

# 前成交价
PHX_FTDC_PSRC_LastPrice = '0'
# 买委托价
PHX_FTDC_PSRC_Buy = '1'
# 卖委托价
PHX_FTDC_PSRC_Sell = '2'

# 激活状态
PHX_FTDC_ACCS_Enable = '0'
# 停止状态
PHX_FTDC_ACCS_Disable = '1'

# 没有执行
PHX_FTDC_OER_NoExec = 'n'
# 已经取消
PHX_FTDC_OER_Canceled = 'c'
# 执行成功
PHX_FTDC_OER_OK = '0'
# 持仓不够
PHX_FTDC_OER_NoPosition = '1'
# 资金不够
PHX_FTDC_OER_NoDeposit = '2'
# 会员不存在
PHX_FTDC_OER_NoParticipant = '3'
# 客户不存在
PHX_FTDC_OER_NoClient = '4'
# 合约不存在
PHX_FTDC_OER_NoInstrument = '6'
# 没有执行权限
PHX_FTDC_OER_NoRight = '7'
# 不合理的数量
PHX_FTDC_OER_InvalidVolume = '8'
# 没有足够的历史成交
PHX_FTDC_OER_NoEnoughHistoryTrade = '9'

# 不合规的持仓强平
PHX_FTDC_AOC_InvalidPositionForceClose = '1'
# 初始化交易会员信用限额
PHX_FTDC_AOC_InitCreditLimit = '2'
# 调整交易会员信用限额
PHX_FTDC_AOC_AlterCreditLimit = '3'
# 取消交易会员信用限额
PHX_FTDC_AOC_CancelCreditLimit = '4'

# 使用历史持仓
PHX_FTDC_PDT_UseHistory = '1'
# 不使用历史持仓
PHX_FTDC_PDT_NoUseHistory = '2'

# 不使用大额单边保证金算法
PHX_FTDC_MMSA_NO = '0'
# 使用大额单边保证金算法
PHX_FTDC_MMSA_YES = '1'

# 正常
PHX_FTDC_CDT_Normal = '0'
# 投机平仓优先
PHX_FTDC_CDT_SpecFirst = '1'

# 不能使用
PHX_FTDC_MFUR_None = '0'
# 用于保证金
PHX_FTDC_MFUR_Margin = '1'
# 用于手续费、盈亏、保证金
PHX_FTDC_MFUR_All = '2'
# 人民币方案3
PHX_FTDC_MFUR_CNY3 = '3'

class CPhxFtdcDisseminationField(object):
    """信息分发"""
    def __init__(self):
        self.SequenceSeries = 0  # 序列系列号, int16_t
        self.SequenceNo = 0  # 序列号, int32_t

    def pack(self):
        return struct.pack('=hi', self.SequenceSeries, 
                           self.SequenceNo)

    def unpack(self, msg):
        unpacks = struct.unpack('=hi', msg)
        self.SequenceSeries = unpacks[0]
        self.SequenceNo = unpacks[1]

    @staticmethod
    def total_length():
        return 6

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcReqAuthenticateField(object):
    """客户端认证请求"""
    def __init__(self):
        self.UserID = 0  # 用户代码, int32_t
        self.AuthData = ""  # 穿透信息(程序自动填写), char[512]
        self.UserProductInfo = ""  # 用户端产品信息 (程序自动填写), char[41]
        self.AppID = ""  # 终端软件AppID, char[30]
        self.AuthCode = ""  # 终端软件授权码, char[20]

    def pack(self):
        return struct.pack('=i512s41s30s20s', self.UserID, 
                           self.AuthData.encode('utf-8'), 
                           self.UserProductInfo.encode('utf-8'), 
                           self.AppID.encode('utf-8'), 
                           self.AuthCode.encode('utf-8'))

    def unpack(self, msg):
        unpacks = struct.unpack('=i512s41s30s20s', msg)
        self.UserID = unpacks[0]
        self.AuthData = unpacks[1].decode('utf-8').rstrip('\0')
        self.UserProductInfo = unpacks[2].decode('utf-8').rstrip('\0')
        self.AppID = unpacks[3].decode('utf-8').rstrip('\0')
        self.AuthCode = unpacks[4].decode('utf-8').rstrip('\0')

    @staticmethod
    def total_length():
        return 607

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcRspAuthenticateField(object):
    """客户端认证响应"""
    def __init__(self):
        self.UserID = 0  # 用户代码, int32_t
        self.AppID = ""  # App代码, char[30]
        self.Token = ""  # 认证成功后返回的Token，登录时需带上, char[30]

    def pack(self):
        return struct.pack('=i30s30s', self.UserID, 
                           self.AppID.encode('utf-8'), 
                           self.Token.encode('utf-8'))

    def unpack(self, msg):
        unpacks = struct.unpack('=i30s30s', msg)
        self.UserID = unpacks[0]
        self.AppID = unpacks[1].decode('utf-8').rstrip('\0')
        self.Token = unpacks[2].decode('utf-8').rstrip('\0')

    @staticmethod
    def total_length():
        return 64

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcReqUserLoginField(object):
    """用户登录请求"""
    def __init__(self):
        self.Session = 0  # Session Number, int16_t
        self.UserID = 0  # 交易用户代码, int32_t
        self.Password = ""  # 密码, char[21]
        self.Token = ""  # Token get from server via CPhxFtdcRspAuthenticateField, char[30]
        self.UserProductInfo = ""  # 用户端产品信息 (程序自动填写), char[41]
        self.InterfaceProductInfo = ""  # 接口端产品信息 (程序自动填写), char[41]
        self.AppID = ""  # 终端软件AppID, char[30]
        self.AuthCode = ""  # 终端软件授权码, char[20]
        self.Reserved0 = ""  # 保留字段, char[45]

    def pack(self):
        return struct.pack('=hi21s30s41s41s30s20s45s', self.Session, 
                           self.UserID, 
                           self.Password.encode('utf-8'), 
                           self.Token.encode('utf-8'), 
                           self.UserProductInfo.encode('utf-8'), 
                           self.InterfaceProductInfo.encode('utf-8'), 
                           self.AppID.encode('utf-8'), 
                           self.AuthCode.encode('utf-8'), 
                           self.Reserved0.encode('utf-8'))

    def unpack(self, msg):
        unpacks = struct.unpack('=hi21s30s41s41s30s20s45s', msg)
        self.Session = unpacks[0]
        self.UserID = unpacks[1]
        self.Password = unpacks[2].decode('utf-8').rstrip('\0')
        self.Token = unpacks[3].decode('utf-8').rstrip('\0')
        self.UserProductInfo = unpacks[4].decode('utf-8').rstrip('\0')
        self.InterfaceProductInfo = unpacks[5].decode('utf-8').rstrip('\0')
        self.AppID = unpacks[6].decode('utf-8').rstrip('\0')
        self.AuthCode = unpacks[7].decode('utf-8').rstrip('\0')
        self.Reserved0 = unpacks[8].decode('utf-8').rstrip('\0')

    @staticmethod
    def total_length():
        return 234

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcRspUserLoginField(object):
    """用户登录应答"""
    def __init__(self):
        self.TradingDay = 0  # 交易日, int32_t
        self.LoginTime = ""  # 登录成功时间, char[9]
        self.MaxOrderLocalID = 0  # 最大本地报单号, int32_t
        self.UserID = 0  # 交易用户代码, int32_t
        self.ParticipantID = ""  # 会员代码, char[11]
        self.TradingSystemName = ""  # 交易系统名称, char[61]
        self.DataCenterID = 0  # 数据中心代码, int32_t
        self.PrivateFlowSize = 0  # 会员私有流当前长度, int32_t
        self.UserFlowSize = 0  # 交易员私有流当前长度, int32_t
        self.Reserved = ""  # 保留字段, char[2]

    def pack(self):
        return struct.pack('=i9sii11s61siii2s', self.TradingDay, 
                           self.LoginTime.encode('utf-8'), 
                           self.MaxOrderLocalID, 
                           self.UserID, 
                           self.ParticipantID.encode('utf-8'), 
                           self.TradingSystemName.encode('utf-8'), 
                           self.DataCenterID, 
                           self.PrivateFlowSize, 
                           self.UserFlowSize, 
                           self.Reserved.encode('utf-8'))

    def unpack(self, msg):
        unpacks = struct.unpack('=i9sii11s61siii2s', msg)
        self.TradingDay = unpacks[0]
        self.LoginTime = unpacks[1].decode('utf-8').rstrip('\0')
        self.MaxOrderLocalID = unpacks[2]
        self.UserID = unpacks[3]
        self.ParticipantID = unpacks[4].decode('utf-8').rstrip('\0')
        self.TradingSystemName = unpacks[5].decode('utf-8').rstrip('\0')
        self.DataCenterID = unpacks[6]
        self.PrivateFlowSize = unpacks[7]
        self.UserFlowSize = unpacks[8]
        self.Reserved = unpacks[9].decode('utf-8').rstrip('\0')

    @staticmethod
    def total_length():
        return 107

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcReqUserLogoutField(object):
    """用户登出请求"""
    def __init__(self):
        self.UserID = 0  # 交易用户代码, int32_t
        self.ParticipantID = ""  # 会员代码, char[11]

    def pack(self):
        return struct.pack('=i11s', self.UserID, 
                           self.ParticipantID.encode('utf-8'))

    def unpack(self, msg):
        unpacks = struct.unpack('=i11s', msg)
        self.UserID = unpacks[0]
        self.ParticipantID = unpacks[1].decode('utf-8').rstrip('\0')

    @staticmethod
    def total_length():
        return 15

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcRspUserLogoutField(object):
    """用户登出应答"""
    def __init__(self):
        self.UserID = 0  # 交易用户代码, int32_t
        self.ParticipantID = ""  # 会员代码, char[11]

    def pack(self):
        return struct.pack('=i11s', self.UserID, 
                           self.ParticipantID.encode('utf-8'))

    def unpack(self, msg):
        unpacks = struct.unpack('=i11s', msg)
        self.UserID = unpacks[0]
        self.ParticipantID = unpacks[1].decode('utf-8').rstrip('\0')

    @staticmethod
    def total_length():
        return 15

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcInputOrderField(object):
    """普通报单录入"""
    def __init__(self):
        self.UserID = 0  # 交易用户代码, int32_t
        self.InvestorID = 0  # 投资者代码, int32_t
        self.InstrumentID = ""  # 合约代码, char[31]
        self.OrderPriceType = chr(0)  # 报单价格条件, char
        self.Direction = chr(0)  # 买卖方向, char
        self.CombOffsetFlag = ""  # 组合开平标志, char[5]
        self.CombHedgeFlag = ""  # 组合投机套保标志, char[5]
        self.LimitPrice = 0  # 价格, double
        self.VolumeTotalOriginal = 0  # 数量, int32_t
        self.TimeCondition = chr(0)  # 有效期类型, char
        self.GTDDate = 0  # GTD日期, int32_t
        self.VolumeCondition = chr(0)  # 成交量类型, char
        self.MinVolume = 0  # 最小成交量, int32_t
        self.ContingentCondition = chr(0)  # 触发条件, char
        self.StopPrice = 0  # 止损价, double
        self.ForceCloseReason = chr(0)  # 强平原因, char
        self.OrderLocalID = 0  # 本地报单编号, int32_t
        self.OrderSysID = 0  # 系统报单编号, int32_t
        self.IsAutoSuspend = 0  # 自动挂起标志, int16_t
        self.ExchangeOrderSysID = ""  # 交易所报单编号, char[13]
        self.ExchangeErrorID = 0  # 交易所错误编号, int32_t

    def pack(self):
        return struct.pack('=ii31scc5s5sdicicicdciih13si', self.UserID, 
                           self.InvestorID, 
                           self.InstrumentID.encode('utf-8'), 
                           self.OrderPriceType.encode('utf-8'), 
                           self.Direction.encode('utf-8'), 
                           self.CombOffsetFlag.encode('utf-8'), 
                           self.CombHedgeFlag.encode('utf-8'), 
                           self.LimitPrice, 
                           self.VolumeTotalOriginal, 
                           self.TimeCondition.encode('utf-8'), 
                           self.GTDDate, 
                           self.VolumeCondition.encode('utf-8'), 
                           self.MinVolume, 
                           self.ContingentCondition.encode('utf-8'), 
                           self.StopPrice, 
                           self.ForceCloseReason.encode('utf-8'), 
                           self.OrderLocalID, 
                           self.OrderSysID, 
                           self.IsAutoSuspend, 
                           self.ExchangeOrderSysID.encode('utf-8'), 
                           self.ExchangeErrorID)

    def unpack(self, msg):
        unpacks = struct.unpack('=ii31scc5s5sdicicicdciih13si', msg)
        self.UserID = unpacks[0]
        self.InvestorID = unpacks[1]
        self.InstrumentID = unpacks[2].decode('utf-8').rstrip('\0')
        self.OrderPriceType = unpacks[3].decode('utf-8').rstrip('\0')
        self.Direction = unpacks[4].decode('utf-8').rstrip('\0')
        self.CombOffsetFlag = unpacks[5].decode('utf-8').rstrip('\0')
        self.CombHedgeFlag = unpacks[6].decode('utf-8').rstrip('\0')
        self.LimitPrice = unpacks[7]
        self.VolumeTotalOriginal = unpacks[8]
        self.TimeCondition = unpacks[9].decode('utf-8').rstrip('\0')
        self.GTDDate = unpacks[10]
        self.VolumeCondition = unpacks[11].decode('utf-8').rstrip('\0')
        self.MinVolume = unpacks[12]
        self.ContingentCondition = unpacks[13].decode('utf-8').rstrip('\0')
        self.StopPrice = unpacks[14]
        self.ForceCloseReason = unpacks[15].decode('utf-8').rstrip('\0')
        self.OrderLocalID = unpacks[16]
        self.OrderSysID = unpacks[17]
        self.IsAutoSuspend = unpacks[18]
        self.ExchangeOrderSysID = unpacks[19].decode('utf-8').rstrip('\0')
        self.ExchangeErrorID = unpacks[20]

    @staticmethod
    def total_length():
        return 110

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcQuickInputOrderField(object):
    """快捷报单录入"""
    def __init__(self):
        self.OrderPriceType = chr(0)  # 报单价格条件, char
        self.Direction = chr(0)  # 买卖方向, char
        self.OffsetFlag = chr(0)  # 开平仓标志, char
        self.HedgeFlag = chr(0)  # 投机套保标志, char
        self.VolumeTotalOriginal = 0  # 数量, int32_t
        self.LimitPrice = 0  # 价格, double
        self.TimeCondition = chr(0)  # 有效期类型, char
        self.VolumeCondition = chr(0)  # 成交量类型, char
        self.MinVolume = 0  # 最小成交量, int16_t
        self.OrderLocalID = 0  # 本地报单编号, int32_t
        self.InstrumentID = ""  # 合约代码, char[13]
        self.Reserved1 = chr(0)  # 保留字段, char
        self.InvestorID = 0  # 投资者代码, int32_t

    def pack(self):
        return struct.pack('=ccccidcchi13sci', self.OrderPriceType.encode('utf-8'), 
                           self.Direction.encode('utf-8'), 
                           self.OffsetFlag.encode('utf-8'), 
                           self.HedgeFlag.encode('utf-8'), 
                           self.VolumeTotalOriginal, 
                           self.LimitPrice, 
                           self.TimeCondition.encode('utf-8'), 
                           self.VolumeCondition.encode('utf-8'), 
                           self.MinVolume, 
                           self.OrderLocalID, 
                           self.InstrumentID.encode('utf-8'), 
                           self.Reserved1.encode('utf-8'), 
                           self.InvestorID)

    def unpack(self, msg):
        unpacks = struct.unpack('=ccccidcchi13sci', msg)
        self.OrderPriceType = unpacks[0].decode('utf-8').rstrip('\0')
        self.Direction = unpacks[1].decode('utf-8').rstrip('\0')
        self.OffsetFlag = unpacks[2].decode('utf-8').rstrip('\0')
        self.HedgeFlag = unpacks[3].decode('utf-8').rstrip('\0')
        self.VolumeTotalOriginal = unpacks[4]
        self.LimitPrice = unpacks[5]
        self.TimeCondition = unpacks[6].decode('utf-8').rstrip('\0')
        self.VolumeCondition = unpacks[7].decode('utf-8').rstrip('\0')
        self.MinVolume = unpacks[8]
        self.OrderLocalID = unpacks[9]
        self.InstrumentID = unpacks[10].decode('utf-8').rstrip('\0')
        self.Reserved1 = unpacks[11].decode('utf-8').rstrip('\0')
        self.InvestorID = unpacks[12]

    @staticmethod
    def total_length():
        return 42

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcOrderActionField(object):
    """报单操作"""
    def __init__(self):
        self.OrderSysID = 0  # 报单编号, int32_t
        self.OrderLocalID = 0  # 本地报单编号, int32_t
        self.UserID = 0  # 交易用户代码, int32_t
        self.InvestorID = 0  # 投资者代码, int32_t
        self.ExchangeErrorID = 0  # 交易所错误编号, int32_t

    def pack(self):
        return struct.pack('=iiiii', self.OrderSysID, 
                           self.OrderLocalID, 
                           self.UserID, 
                           self.InvestorID, 
                           self.ExchangeErrorID)

    def unpack(self, msg):
        unpacks = struct.unpack('=iiiii', msg)
        self.OrderSysID = unpacks[0]
        self.OrderLocalID = unpacks[1]
        self.UserID = unpacks[2]
        self.InvestorID = unpacks[3]
        self.ExchangeErrorID = unpacks[4]

    @staticmethod
    def total_length():
        return 20

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcQryOrderField(object):
    """报单查询"""
    def __init__(self):
        self.InvestorID = 0  # 投资者代码, int32_t
        self.InstrumentID = ""  # 合约代码, char[13]
        self.OrderSysID = 0  # 报单编号, int32_t
        self.StartIndex = 0  # 报单开始序号（从0开始）, int32_t
        self.EndIndex = 0  # 报单结束序号（不包含，开区间）, int32_t
        self.ExchangeDescriptor = 0  # 交易所描述符, uint8_t

    def pack(self):
        return struct.pack('=i13siiiB', self.InvestorID, 
                           self.InstrumentID.encode('utf-8'), 
                           self.OrderSysID, 
                           self.StartIndex, 
                           self.EndIndex, 
                           self.ExchangeDescriptor)

    def unpack(self, msg):
        unpacks = struct.unpack('=i13siiiB', msg)
        self.InvestorID = unpacks[0]
        self.InstrumentID = unpacks[1].decode('utf-8').rstrip('\0')
        self.OrderSysID = unpacks[2]
        self.StartIndex = unpacks[3]
        self.EndIndex = unpacks[4]
        self.ExchangeDescriptor = unpacks[5]

    @staticmethod
    def total_length():
        return 30

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcQryTradeField(object):
    """成交查询"""
    def __init__(self):
        self.InvestorID = 0  # 投资者代码, int32_t
        self.InstrumentID = ""  # 合约代码, char[13]
        self.TradeID = 0  # 成交编号, int32_t
        self.StartIndex = 0  # 成交开始序号（从0开始）, int32_t
        self.EndIndex = 0  # 报单结束序号（不包含，开区间）, int32_t
        self.ExchangeDescriptor = 0  # 交易所描述符, uint8_t

    def pack(self):
        return struct.pack('=i13siiiB', self.InvestorID, 
                           self.InstrumentID.encode('utf-8'), 
                           self.TradeID, 
                           self.StartIndex, 
                           self.EndIndex, 
                           self.ExchangeDescriptor)

    def unpack(self, msg):
        unpacks = struct.unpack('=i13siiiB', msg)
        self.InvestorID = unpacks[0]
        self.InstrumentID = unpacks[1].decode('utf-8').rstrip('\0')
        self.TradeID = unpacks[2]
        self.StartIndex = unpacks[3]
        self.EndIndex = unpacks[4]
        self.ExchangeDescriptor = unpacks[5]

    @staticmethod
    def total_length():
        return 30

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcQryMarketDataField(object):
    """行情查询"""
    def __init__(self):
        self.ProductID = ""  # 产品代码, char[9]
        self.InstrumentID = ""  # 合约代码, char[13]

    def pack(self):
        return struct.pack('=9s13s', self.ProductID.encode('utf-8'), 
                           self.InstrumentID.encode('utf-8'))

    def unpack(self, msg):
        unpacks = struct.unpack('=9s13s', msg)
        self.ProductID = unpacks[0].decode('utf-8').rstrip('\0')
        self.InstrumentID = unpacks[1].decode('utf-8').rstrip('\0')

    @staticmethod
    def total_length():
        return 22

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcQryClientPositionField(object):
    """客户持仓查询"""
    def __init__(self):
        self.InvestorID = 0  # 投资者代码, int32_t
        self.InstrumentID = ""  # 合约代码, char[13]
        self.ExchangeDescriptor = 0  # 交易所描述符, uint8_t

    def pack(self):
        return struct.pack('=i13sB', self.InvestorID, 
                           self.InstrumentID.encode('utf-8'), 
                           self.ExchangeDescriptor)

    def unpack(self, msg):
        unpacks = struct.unpack('=i13sB', msg)
        self.InvestorID = unpacks[0]
        self.InstrumentID = unpacks[1].decode('utf-8').rstrip('\0')
        self.ExchangeDescriptor = unpacks[2]

    @staticmethod
    def total_length():
        return 18

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcQryProductField(object):
    """产品查询"""
    def __init__(self):
        self.ProductID = ""  # 产品代码, char[9]

    def pack(self):
        return struct.pack('=9s', self.ProductID.encode('utf-8'))

    def unpack(self, msg):
        unpacks = struct.unpack('=9s', msg)
        self.ProductID = unpacks[0].decode('utf-8').rstrip('\0')

    @staticmethod
    def total_length():
        return 9

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcQryInstrumentField(object):
    """合约查询"""
    def __init__(self):
        self.ProductID = ""  # 产品代码, char[9]
        self.InstrumentID = ""  # 合约代码, char[13]

    def pack(self):
        return struct.pack('=9s13s', self.ProductID.encode('utf-8'), 
                           self.InstrumentID.encode('utf-8'))

    def unpack(self, msg):
        unpacks = struct.unpack('=9s13s', msg)
        self.ProductID = unpacks[0].decode('utf-8').rstrip('\0')
        self.InstrumentID = unpacks[1].decode('utf-8').rstrip('\0')

    @staticmethod
    def total_length():
        return 22

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcRspClientPositionField(object):
    """客户持仓"""
    def __init__(self):
        self.HedgeFlag = chr(0)  # 投机套保标志, char
        self.PosiDirection = chr(0)  # 持仓多空方向, char
        self.InitYdPosition = 0  # 上日初始持仓, int32_t
        self.YdPosition = 0  # 上日持仓, int32_t
        self.Position = 0  # 今日持仓, int32_t
        self.YdPositionFrozen = 0  # 昨日持仓冻结, int32_t
        self.PositionFrozen = 0  # 今日持仓冻结, int32_t
        self.TotalPositionFrozen = 0  # 总冻结持仓, int32_t
        self.LongFrozen = 0  # 多头冻结, int32_t
        self.ShortFrozen = 0  # 空头冻结, int32_t
        self.YdLongFrozen = 0  # 昨日多头冻结, int32_t
        self.YdShortFrozen = 0  # 昨日空头冻结, int32_t
        self.PositionCost = 0  # 持仓成本, double
        self.YdPositionCost = 0  # 昨日持仓成本, double
        self.UseMargin = 0  # 占用的保证金, double
        self.InstrumentID = ""  # 合约代码, char[31]
        self.InvestorID = 0  # 投资者代码, int32_t

    def pack(self):
        return struct.pack('=cciiiiiiiiiiddd31si', self.HedgeFlag.encode('utf-8'), 
                           self.PosiDirection.encode('utf-8'), 
                           self.InitYdPosition, 
                           self.YdPosition, 
                           self.Position, 
                           self.YdPositionFrozen, 
                           self.PositionFrozen, 
                           self.TotalPositionFrozen, 
                           self.LongFrozen, 
                           self.ShortFrozen, 
                           self.YdLongFrozen, 
                           self.YdShortFrozen, 
                           self.PositionCost, 
                           self.YdPositionCost, 
                           self.UseMargin, 
                           self.InstrumentID.encode('utf-8'), 
                           self.InvestorID)

    def unpack(self, msg):
        unpacks = struct.unpack('=cciiiiiiiiiiddd31si', msg)
        self.HedgeFlag = unpacks[0].decode('utf-8').rstrip('\0')
        self.PosiDirection = unpacks[1].decode('utf-8').rstrip('\0')
        self.InitYdPosition = unpacks[2]
        self.YdPosition = unpacks[3]
        self.Position = unpacks[4]
        self.YdPositionFrozen = unpacks[5]
        self.PositionFrozen = unpacks[6]
        self.TotalPositionFrozen = unpacks[7]
        self.LongFrozen = unpacks[8]
        self.ShortFrozen = unpacks[9]
        self.YdLongFrozen = unpacks[10]
        self.YdShortFrozen = unpacks[11]
        self.PositionCost = unpacks[12]
        self.YdPositionCost = unpacks[13]
        self.UseMargin = unpacks[14]
        self.InstrumentID = unpacks[15].decode('utf-8').rstrip('\0')
        self.InvestorID = unpacks[16]

    @staticmethod
    def total_length():
        return 101

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcProductField(object):
    """产品"""
    def __init__(self):
        self.ProductID = ""  # 产品代码, char[9]
        self.ProductName = ""  # 产品名称, char[21]
        self.ExchangeID = ""  # 交易所代码, char[9]
        self.ProductClass = chr(0)  # 产品类型, char
        self.VolumeMultiple = 0  # 合约数量乘数, int32_t
        self.PriceTick = 0  # 最小变动价位, double
        self.MaxMarketOrderVolume = 0  # 市价单最大下单量, int32_t
        self.MinMarketOrderVolume = 0  # 市价单最小下单量, int32_t
        self.MaxLimitOrderVolume = 0  # 限价单最大下单量, int32_t
        self.MinLimitOrderVolume = 0  # 限价单最小下单量, int32_t
        self.PositionType = chr(0)  # 持仓类型, char
        self.PositionDateType = chr(0)  # 持仓日期类型, char
        self.CloseDealType = chr(0)  # 平仓处理类型, char
        self.TradeCurrencyID = ""  # 交易币种类型, char[4]
        self.MortgageFundUseRange = chr(0)  # 质押资金可用范围, char
        self.ExchangeProductID = ""  # 交易所产品代码, char[13]
        self.UnderlyingMultiple = 0  # 合约基础商品乘数, double

    def pack(self):
        return struct.pack('=9s21s9scidiiiiccc4sc13sd', self.ProductID.encode('utf-8'), 
                           self.ProductName.encode('utf-8'), 
                           self.ExchangeID.encode('utf-8'), 
                           self.ProductClass.encode('utf-8'), 
                           self.VolumeMultiple, 
                           self.PriceTick, 
                           self.MaxMarketOrderVolume, 
                           self.MinMarketOrderVolume, 
                           self.MaxLimitOrderVolume, 
                           self.MinLimitOrderVolume, 
                           self.PositionType.encode('utf-8'), 
                           self.PositionDateType.encode('utf-8'), 
                           self.CloseDealType.encode('utf-8'), 
                           self.TradeCurrencyID.encode('utf-8'), 
                           self.MortgageFundUseRange.encode('utf-8'), 
                           self.ExchangeProductID.encode('utf-8'), 
                           self.UnderlyingMultiple)

    def unpack(self, msg):
        unpacks = struct.unpack('=9s21s9scidiiiiccc4sc13sd', msg)
        self.ProductID = unpacks[0].decode('utf-8').rstrip('\0')
        self.ProductName = unpacks[1].decode('utf-8').rstrip('\0')
        self.ExchangeID = unpacks[2].decode('utf-8').rstrip('\0')
        self.ProductClass = unpacks[3].decode('utf-8').rstrip('\0')
        self.VolumeMultiple = unpacks[4]
        self.PriceTick = unpacks[5]
        self.MaxMarketOrderVolume = unpacks[6]
        self.MinMarketOrderVolume = unpacks[7]
        self.MaxLimitOrderVolume = unpacks[8]
        self.MinLimitOrderVolume = unpacks[9]
        self.PositionType = unpacks[10].decode('utf-8').rstrip('\0')
        self.PositionDateType = unpacks[11].decode('utf-8').rstrip('\0')
        self.CloseDealType = unpacks[12].decode('utf-8').rstrip('\0')
        self.TradeCurrencyID = unpacks[13].decode('utf-8').rstrip('\0')
        self.MortgageFundUseRange = unpacks[14].decode('utf-8').rstrip('\0')
        self.ExchangeProductID = unpacks[15].decode('utf-8').rstrip('\0')
        self.UnderlyingMultiple = unpacks[16]

    @staticmethod
    def total_length():
        return 97

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcRspInstrumentField(object):
    """合约"""
    def __init__(self):
        self.ProductID = ""  # 产品代码, char[9]
        self.ProductGroupID = ""  # 产品组代码, char[9]
        self.UnderlyingInstrID = ""  # 基础商品代码, char[13]
        self.ProductClass = chr(0)  # 产品类型, char
        self.PositionType = chr(0)  # 持仓类型, char
        self.StrikePrice = 0  # 执行价, double
        self.VolumeMultiple = 0  # 合约数量乘数, int32_t
        self.UnderlyingMultiple = 0  # 合约基础商品乘数, double
        self.InstrumentID = ""  # 合约代码, char[31]
        self.InstrumentName = ""  # 合约名称, char[21]
        self.DeliveryYear = 0  # 交割年份, int32_t
        self.DeliveryMonth = 0  # 交割月, int32_t
        self.AdvanceMonth = ""  # 提前月份, char[4]
        self.IsTrading = 0  # 当前是否交易, int16_t
        self.CreateDate = 0  # 创建日, int32_t
        self.OpenDate = 0  # 上市日, int32_t
        self.ExpireDate = 0  # 到期日, int32_t
        self.StartDelivDate = 0  # 开始交割日, int32_t
        self.EndDelivDate = 0  # 最后交割日, int32_t
        self.BasisPrice = 0  # 挂牌基准价, double
        self.MaxMarketOrderVolume = 0  # 市价单最大下单量, int32_t
        self.MinMarketOrderVolume = 0  # 市价单最小下单量, int32_t
        self.MaxLimitOrderVolume = 0  # 限价单最大下单量, int32_t
        self.MinLimitOrderVolume = 0  # 限价单最小下单量, int32_t
        self.PriceTick = 0  # 最小变动价位, double
        self.AllowDelivPersonOpen = 0  # 交割月自然人开仓, int32_t

    def pack(self):
        return struct.pack('=9s9s13sccdid31s21sii4shiiiiidiiiidi', self.ProductID.encode('utf-8'), 
                           self.ProductGroupID.encode('utf-8'), 
                           self.UnderlyingInstrID.encode('utf-8'), 
                           self.ProductClass.encode('utf-8'), 
                           self.PositionType.encode('utf-8'), 
                           self.StrikePrice, 
                           self.VolumeMultiple, 
                           self.UnderlyingMultiple, 
                           self.InstrumentID.encode('utf-8'), 
                           self.InstrumentName.encode('utf-8'), 
                           self.DeliveryYear, 
                           self.DeliveryMonth, 
                           self.AdvanceMonth.encode('utf-8'), 
                           self.IsTrading, 
                           self.CreateDate, 
                           self.OpenDate, 
                           self.ExpireDate, 
                           self.StartDelivDate, 
                           self.EndDelivDate, 
                           self.BasisPrice, 
                           self.MaxMarketOrderVolume, 
                           self.MinMarketOrderVolume, 
                           self.MaxLimitOrderVolume, 
                           self.MinLimitOrderVolume, 
                           self.PriceTick, 
                           self.AllowDelivPersonOpen)

    def unpack(self, msg):
        unpacks = struct.unpack('=9s9s13sccdid31s21sii4shiiiiidiiiidi', msg)
        self.ProductID = unpacks[0].decode('utf-8').rstrip('\0')
        self.ProductGroupID = unpacks[1].decode('utf-8').rstrip('\0')
        self.UnderlyingInstrID = unpacks[2].decode('utf-8').rstrip('\0')
        self.ProductClass = unpacks[3].decode('utf-8').rstrip('\0')
        self.PositionType = unpacks[4].decode('utf-8').rstrip('\0')
        self.StrikePrice = unpacks[5]
        self.VolumeMultiple = unpacks[6]
        self.UnderlyingMultiple = unpacks[7]
        self.InstrumentID = unpacks[8].decode('utf-8').rstrip('\0')
        self.InstrumentName = unpacks[9].decode('utf-8').rstrip('\0')
        self.DeliveryYear = unpacks[10]
        self.DeliveryMonth = unpacks[11]
        self.AdvanceMonth = unpacks[12].decode('utf-8').rstrip('\0')
        self.IsTrading = unpacks[13]
        self.CreateDate = unpacks[14]
        self.OpenDate = unpacks[15]
        self.ExpireDate = unpacks[16]
        self.StartDelivDate = unpacks[17]
        self.EndDelivDate = unpacks[18]
        self.BasisPrice = unpacks[19]
        self.MaxMarketOrderVolume = unpacks[20]
        self.MinMarketOrderVolume = unpacks[21]
        self.MaxLimitOrderVolume = unpacks[22]
        self.MinLimitOrderVolume = unpacks[23]
        self.PriceTick = unpacks[24]
        self.AllowDelivPersonOpen = unpacks[25]

    @staticmethod
    def total_length():
        return 175

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcInstrumentField(object):
    """Ffex合约"""
    def __init__(self):
        self.ProductID = ""  # 产品代码, char[9]
        self.ProductGroupID = ""  # 产品组代码, char[9]
        self.UnderlyingInstrID = ""  # 基础商品代码, char[13]
        self.ProductClass = chr(0)  # 产品类型, char
        self.PositionType = chr(0)  # 持仓类型, char
        self.StrikePrice = 0  # 执行价, double
        self.VolumeMultiple = 0  # 合约数量乘数, int32_t
        self.UnderlyingMultiple = 0  # 合约基础商品乘数, double
        self.InstrumentID = ""  # 合约代码, char[13]
        self.InstrumentName = ""  # 合约名称, char[21]
        self.DeliveryYear = 0  # 交割年份, int32_t
        self.DeliveryMonth = 0  # 交割月, int32_t
        self.AdvanceMonth = ""  # 提前月份, char[4]
        self.IsTrading = 0  # 当前是否交易, int16_t

    def pack(self):
        return struct.pack('=9s9s13sccdid13s21sii4sh', self.ProductID.encode('utf-8'), 
                           self.ProductGroupID.encode('utf-8'), 
                           self.UnderlyingInstrID.encode('utf-8'), 
                           self.ProductClass.encode('utf-8'), 
                           self.PositionType.encode('utf-8'), 
                           self.StrikePrice, 
                           self.VolumeMultiple, 
                           self.UnderlyingMultiple, 
                           self.InstrumentID.encode('utf-8'), 
                           self.InstrumentName.encode('utf-8'), 
                           self.DeliveryYear, 
                           self.DeliveryMonth, 
                           self.AdvanceMonth.encode('utf-8'), 
                           self.IsTrading)

    def unpack(self, msg):
        unpacks = struct.unpack('=9s9s13sccdid13s21sii4sh', msg)
        self.ProductID = unpacks[0].decode('utf-8').rstrip('\0')
        self.ProductGroupID = unpacks[1].decode('utf-8').rstrip('\0')
        self.UnderlyingInstrID = unpacks[2].decode('utf-8').rstrip('\0')
        self.ProductClass = unpacks[3].decode('utf-8').rstrip('\0')
        self.PositionType = unpacks[4].decode('utf-8').rstrip('\0')
        self.StrikePrice = unpacks[5]
        self.VolumeMultiple = unpacks[6]
        self.UnderlyingMultiple = unpacks[7]
        self.InstrumentID = unpacks[8].decode('utf-8').rstrip('\0')
        self.InstrumentName = unpacks[9].decode('utf-8').rstrip('\0')
        self.DeliveryYear = unpacks[10]
        self.DeliveryMonth = unpacks[11]
        self.AdvanceMonth = unpacks[12].decode('utf-8').rstrip('\0')
        self.IsTrading = unpacks[13]

    @staticmethod
    def total_length():
        return 101

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcDepthMarketDataField(object):
    """深度市场行情"""
    def __init__(self):
        self.LastPrice = 0  # 最新价, double
        self.LastVolume = 0  # 数量, int32_t
        self.ExchangeTime = 0  # 时间, int32_t
        self.InstrumentID = ""  # 合约代码, char[13]
        self.BidPrice1 = 0  # 申买价一, double
        self.BidVolume1 = 0  # 申买量一, int32_t
        self.AskPrice1 = 0  # 申卖价一, double
        self.AskVolume1 = 0  # 申卖量一, int32_t
        self.BidPrice2 = 0  # 申买价二, double
        self.BidVolume2 = 0  # 申买量二, int32_t
        self.AskPrice2 = 0  # 申卖价二, double
        self.AskVolume2 = 0  # 申卖量二, int32_t
        self.BidPrice3 = 0  # 申买价三, double
        self.BidVolume3 = 0  # 申买量三, int32_t
        self.AskPrice3 = 0  # 申卖价三, double
        self.AskVolume3 = 0  # 申卖量三, int32_t
        self.BidPrice4 = 0  # 申买价四, double
        self.BidVolume4 = 0  # 申买量四, int32_t
        self.AskPrice4 = 0  # 申卖价四, double
        self.AskVolume4 = 0  # 申卖量四, int32_t
        self.BidPrice5 = 0  # 申买价五, double
        self.BidVolume5 = 0  # 申买量五, int32_t
        self.AskPrice5 = 0  # 申卖价五, double
        self.AskVolume5 = 0  # 申卖量五, int32_t

    def pack(self):
        return struct.pack('=dii13sdidididididididididi', self.LastPrice, 
                           self.LastVolume, 
                           self.ExchangeTime, 
                           self.InstrumentID.encode('utf-8'), 
                           self.BidPrice1, 
                           self.BidVolume1, 
                           self.AskPrice1, 
                           self.AskVolume1, 
                           self.BidPrice2, 
                           self.BidVolume2, 
                           self.AskPrice2, 
                           self.AskVolume2, 
                           self.BidPrice3, 
                           self.BidVolume3, 
                           self.AskPrice3, 
                           self.AskVolume3, 
                           self.BidPrice4, 
                           self.BidVolume4, 
                           self.AskPrice4, 
                           self.AskVolume4, 
                           self.BidPrice5, 
                           self.BidVolume5, 
                           self.AskPrice5, 
                           self.AskVolume5)

    def unpack(self, msg):
        unpacks = struct.unpack('=dii13sdidididididididididi', msg)
        self.LastPrice = unpacks[0]
        self.LastVolume = unpacks[1]
        self.ExchangeTime = unpacks[2]
        self.InstrumentID = unpacks[3].decode('utf-8').rstrip('\0')
        self.BidPrice1 = unpacks[4]
        self.BidVolume1 = unpacks[5]
        self.AskPrice1 = unpacks[6]
        self.AskVolume1 = unpacks[7]
        self.BidPrice2 = unpacks[8]
        self.BidVolume2 = unpacks[9]
        self.AskPrice2 = unpacks[10]
        self.AskVolume2 = unpacks[11]
        self.BidPrice3 = unpacks[12]
        self.BidVolume3 = unpacks[13]
        self.AskPrice3 = unpacks[14]
        self.AskVolume3 = unpacks[15]
        self.BidPrice4 = unpacks[16]
        self.BidVolume4 = unpacks[17]
        self.AskPrice4 = unpacks[18]
        self.AskVolume4 = unpacks[19]
        self.BidPrice5 = unpacks[20]
        self.BidVolume5 = unpacks[21]
        self.AskPrice5 = unpacks[22]
        self.AskVolume5 = unpacks[23]

    @staticmethod
    def total_length():
        return 149

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcOrderField(object):
    """报单"""
    def __init__(self):
        self.OrderSysID = 0  # 报单编号, int32_t
        self.InvestorID = 0  # 投资者代码, int32_t
        self.InstrumentID = ""  # 合约代码, char[31]
        self.OrderPriceType = chr(0)  # 报单价格条件, char
        self.Direction = chr(0)  # 买卖方向, char
        self.CombOffsetFlag = ""  # 组合开平标志, char[5]
        self.CombHedgeFlag = ""  # 组合投机套保标志, char[5]
        self.LimitPrice = 0  # 价格, double
        self.VolumeTotalOriginal = 0  # 数量, int32_t
        self.TimeCondition = chr(0)  # 有效期类型, char
        self.VolumeCondition = chr(0)  # 成交量类型, char
        self.MinVolume = 0  # 最小成交量, int32_t
        self.ContingentCondition = chr(0)  # 触发条件, char
        self.StopPrice = 0  # 止损价, double
        self.ForceCloseReason = chr(0)  # 强平原因, char
        self.OrderLocalID = 0  # 本地报单编号, int32_t
        self.IsAutoSuspend = 0  # 自动挂起标志, int16_t
        self.OrderStatus = chr(0)  # 报单状态, char
        self.VolumeTraded = 0  # 今成交数量, int32_t
        self.VolumeTotal = 0  # 剩余数量, int32_t
        self.InsertTimeStamp = 0  # 报单插入时间, int64_t
        self.ExchUpdateTime = ""  # 最后修改时间 (以交易所回报时间为准）, char[9]
        self.ExchangeOrderSysID = ""  # 交易所报单编号, char[13]
        self.ExchangeErrorID = 0  # 交易所错误码, int32_t
        self.OrderIndex = 0  # 报单序号（仅在按Index查询的回报中有效）, int32_t

    def pack(self):
        return struct.pack('=ii31scc5s5sdiccicdcihciiq9s13sii', self.OrderSysID, 
                           self.InvestorID, 
                           self.InstrumentID.encode('utf-8'), 
                           self.OrderPriceType.encode('utf-8'), 
                           self.Direction.encode('utf-8'), 
                           self.CombOffsetFlag.encode('utf-8'), 
                           self.CombHedgeFlag.encode('utf-8'), 
                           self.LimitPrice, 
                           self.VolumeTotalOriginal, 
                           self.TimeCondition.encode('utf-8'), 
                           self.VolumeCondition.encode('utf-8'), 
                           self.MinVolume, 
                           self.ContingentCondition.encode('utf-8'), 
                           self.StopPrice, 
                           self.ForceCloseReason.encode('utf-8'), 
                           self.OrderLocalID, 
                           self.IsAutoSuspend, 
                           self.OrderStatus.encode('utf-8'), 
                           self.VolumeTraded, 
                           self.VolumeTotal, 
                           self.InsertTimeStamp, 
                           self.ExchUpdateTime.encode('utf-8'), 
                           self.ExchangeOrderSysID.encode('utf-8'), 
                           self.ExchangeErrorID, 
                           self.OrderIndex)

    def unpack(self, msg):
        unpacks = struct.unpack('=ii31scc5s5sdiccicdcihciiq9s13sii', msg)
        self.OrderSysID = unpacks[0]
        self.InvestorID = unpacks[1]
        self.InstrumentID = unpacks[2].decode('utf-8').rstrip('\0')
        self.OrderPriceType = unpacks[3].decode('utf-8').rstrip('\0')
        self.Direction = unpacks[4].decode('utf-8').rstrip('\0')
        self.CombOffsetFlag = unpacks[5].decode('utf-8').rstrip('\0')
        self.CombHedgeFlag = unpacks[6].decode('utf-8').rstrip('\0')
        self.LimitPrice = unpacks[7]
        self.VolumeTotalOriginal = unpacks[8]
        self.TimeCondition = unpacks[9].decode('utf-8').rstrip('\0')
        self.VolumeCondition = unpacks[10].decode('utf-8').rstrip('\0')
        self.MinVolume = unpacks[11]
        self.ContingentCondition = unpacks[12].decode('utf-8').rstrip('\0')
        self.StopPrice = unpacks[13]
        self.ForceCloseReason = unpacks[14].decode('utf-8').rstrip('\0')
        self.OrderLocalID = unpacks[15]
        self.IsAutoSuspend = unpacks[16]
        self.OrderStatus = unpacks[17].decode('utf-8').rstrip('\0')
        self.VolumeTraded = unpacks[18]
        self.VolumeTotal = unpacks[19]
        self.InsertTimeStamp = unpacks[20]
        self.ExchUpdateTime = unpacks[21].decode('utf-8').rstrip('\0')
        self.ExchangeOrderSysID = unpacks[22].decode('utf-8').rstrip('\0')
        self.ExchangeErrorID = unpacks[23]
        self.OrderIndex = unpacks[24]

    @staticmethod
    def total_length():
        return 132

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcTradeField(object):
    """成交"""
    def __init__(self):
        self.TradeID = 0  # 成交编号, int32_t
        self.InstrumentID = ""  # 合约代码, char[13]
        self.OrderSysID = 0  # 报单编号, int32_t
        self.InvestorID = 0  # 投资者代码, int32_t
        self.Price = 0  # 价格, double
        self.Volume = 0  # 数量, int32_t
        self.OffsetFlag = chr(0)  # 开平标志, char
        self.Direction = chr(0)  # 买卖方向, char
        self.TradeTime = ""  # 成交时间, char[9]
        self.OrderLocalID = 0  # 本地报单编号, int32_t
        self.ExchangeOrderSysID = ""  # 交易所报单编号, char[13]
        self.TradeIndex = 0  # 成交序号（仅在按Index查询的回报中有效）, int32_t

    def pack(self):
        return struct.pack('=i13siidicc9si13si', self.TradeID, 
                           self.InstrumentID.encode('utf-8'), 
                           self.OrderSysID, 
                           self.InvestorID, 
                           self.Price, 
                           self.Volume, 
                           self.OffsetFlag.encode('utf-8'), 
                           self.Direction.encode('utf-8'), 
                           self.TradeTime.encode('utf-8'), 
                           self.OrderLocalID, 
                           self.ExchangeOrderSysID.encode('utf-8'), 
                           self.TradeIndex)

    def unpack(self, msg):
        unpacks = struct.unpack('=i13siidicc9si13si', msg)
        self.TradeID = unpacks[0]
        self.InstrumentID = unpacks[1].decode('utf-8').rstrip('\0')
        self.OrderSysID = unpacks[2]
        self.InvestorID = unpacks[3]
        self.Price = unpacks[4]
        self.Volume = unpacks[5]
        self.OffsetFlag = unpacks[6].decode('utf-8').rstrip('\0')
        self.Direction = unpacks[7].decode('utf-8').rstrip('\0')
        self.TradeTime = unpacks[8].decode('utf-8').rstrip('\0')
        self.OrderLocalID = unpacks[9]
        self.ExchangeOrderSysID = unpacks[10].decode('utf-8').rstrip('\0')
        self.TradeIndex = unpacks[11]

    @staticmethod
    def total_length():
        return 69

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcQryInstrumentStatusField(object):
    """查询合约状态"""
    def __init__(self):
        self.ExchangeID = ""  # 交易所代码, char[9]
        self.InstrumentID = ""  # 合约代码, char[13]

    def pack(self):
        return struct.pack('=9s13s', self.ExchangeID.encode('utf-8'), 
                           self.InstrumentID.encode('utf-8'))

    def unpack(self, msg):
        unpacks = struct.unpack('=9s13s', msg)
        self.ExchangeID = unpacks[0].decode('utf-8').rstrip('\0')
        self.InstrumentID = unpacks[1].decode('utf-8').rstrip('\0')

    @staticmethod
    def total_length():
        return 22

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcInstrumentStatusField(object):
    """合约状态"""
    def __init__(self):
        self.ExchangeID = ""  # 交易所代码, char[9]
        self.InstrumentID = ""  # 合约代码, char[13]
        self.InstrumentStatus = chr(0)  # 合约交易状态, char
        self.TradingSegmentSN = 0  # 交易阶段编号, int32_t
        self.EnterTime = ""  # 进入本状态时间, char[9]
        self.EnterReason = chr(0)  # 进入本状态原因, char

    def pack(self):
        return struct.pack('=9s13sci9sc', self.ExchangeID.encode('utf-8'), 
                           self.InstrumentID.encode('utf-8'), 
                           self.InstrumentStatus.encode('utf-8'), 
                           self.TradingSegmentSN, 
                           self.EnterTime.encode('utf-8'), 
                           self.EnterReason.encode('utf-8'))

    def unpack(self, msg):
        unpacks = struct.unpack('=9s13sci9sc', msg)
        self.ExchangeID = unpacks[0].decode('utf-8').rstrip('\0')
        self.InstrumentID = unpacks[1].decode('utf-8').rstrip('\0')
        self.InstrumentStatus = unpacks[2].decode('utf-8').rstrip('\0')
        self.TradingSegmentSN = unpacks[3]
        self.EnterTime = unpacks[4].decode('utf-8').rstrip('\0')
        self.EnterReason = unpacks[5].decode('utf-8').rstrip('\0')

    @staticmethod
    def total_length():
        return 37

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcQryClientAccountField(object):
    """客户资金查询"""
    def __init__(self):
        self.InvestorID = 0  # 投资者代码, int32_t

    def pack(self):
        return struct.pack('=i', self.InvestorID)

    def unpack(self, msg):
        unpacks = struct.unpack('=i', msg)
        self.InvestorID = unpacks[0]

    @staticmethod
    def total_length():
        return 4

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcRspClientAccountField(object):
    """客户资金"""
    def __init__(self):
        self.InvestorID = 0  # 投资者代码, int32_t
        self.PreBalance = 0  # 上次结算准备金, double
        self.CurrMargin = 0  # 当前保证金总额, double
        self.CurrCommission = 0  # 当前手续费, double
        self.FloatProfit = 0  # 浮动盈亏, double
        self.CloseProfit = 0  # 平仓盈亏, double
        self.Deposit = 0  # 入金金额, double
        self.Withdraw = 0  # 出金金额, double
        self.Balance = 0  # 期货结算准备金, double
        self.Available = 0  # 可用资金, double
        self.FrozenMargin = 0  # 冻结的保证金, double
        self.FrozenCommission = 0  # 冻结的手续费, double
        self.TotalMarketMakingCount = 0  # 做市义务总量, uint32_t
        self.TotalMarketMakingCompleteCount = 0  # 做市义务完成总量, uint32_t
        self.TotalOptionTradeCount = 0  # 期权总成交量, uint32_t

    def pack(self):
        return struct.pack('=idddddddddddIII', self.InvestorID, 
                           self.PreBalance, 
                           self.CurrMargin, 
                           self.CurrCommission, 
                           self.FloatProfit, 
                           self.CloseProfit, 
                           self.Deposit, 
                           self.Withdraw, 
                           self.Balance, 
                           self.Available, 
                           self.FrozenMargin, 
                           self.FrozenCommission, 
                           self.TotalMarketMakingCount, 
                           self.TotalMarketMakingCompleteCount, 
                           self.TotalOptionTradeCount)

    def unpack(self, msg):
        unpacks = struct.unpack('=idddddddddddIII', msg)
        self.InvestorID = unpacks[0]
        self.PreBalance = unpacks[1]
        self.CurrMargin = unpacks[2]
        self.CurrCommission = unpacks[3]
        self.FloatProfit = unpacks[4]
        self.CloseProfit = unpacks[5]
        self.Deposit = unpacks[6]
        self.Withdraw = unpacks[7]
        self.Balance = unpacks[8]
        self.Available = unpacks[9]
        self.FrozenMargin = unpacks[10]
        self.FrozenCommission = unpacks[11]
        self.TotalMarketMakingCount = unpacks[12]
        self.TotalMarketMakingCompleteCount = unpacks[13]
        self.TotalOptionTradeCount = unpacks[14]

    @staticmethod
    def total_length():
        return 104

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcQryInstrumentMarginRateField(object):
    """合约保证金率查询"""
    def __init__(self):
        self.InstrumentID = ""  # 合约代码, char[13]
        self.InvestorID = 0  # 投资者代码, int32_t
        self.HedgeFlag = chr(0)  # 投机套保标志, char

    def pack(self):
        return struct.pack('=13sic', self.InstrumentID.encode('utf-8'), 
                           self.InvestorID, 
                           self.HedgeFlag.encode('utf-8'))

    def unpack(self, msg):
        unpacks = struct.unpack('=13sic', msg)
        self.InstrumentID = unpacks[0].decode('utf-8').rstrip('\0')
        self.InvestorID = unpacks[1]
        self.HedgeFlag = unpacks[2].decode('utf-8').rstrip('\0')

    @staticmethod
    def total_length():
        return 18

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcRspInstrumentMarginRateField(object):
    """合约保证金率查询回报"""
    def __init__(self):
        self.InstrumentID = ""  # 合约代码, char[13]
        self.InvestorID = 0  # 投资者代码, int32_t
        self.HedgeFlag = chr(0)  # 投机套保标志, char
        self.LongMarginRatioByMoney = 0  # 多头保证金率, double
        self.LongMarginRatioByVolume = 0  # 多头保证金费, double
        self.ShortMarginRatioByMoney = 0  # 空头保证金率, double
        self.ShortMarginRatioByVolume = 0  # 空头保证金费, double
        self.IsRelative = 0  # 是否相对交易所收取, int16_t

    def pack(self):
        return struct.pack('=13sicddddh', self.InstrumentID.encode('utf-8'), 
                           self.InvestorID, 
                           self.HedgeFlag.encode('utf-8'), 
                           self.LongMarginRatioByMoney, 
                           self.LongMarginRatioByVolume, 
                           self.ShortMarginRatioByMoney, 
                           self.ShortMarginRatioByVolume, 
                           self.IsRelative)

    def unpack(self, msg):
        unpacks = struct.unpack('=13sicddddh', msg)
        self.InstrumentID = unpacks[0].decode('utf-8').rstrip('\0')
        self.InvestorID = unpacks[1]
        self.HedgeFlag = unpacks[2].decode('utf-8').rstrip('\0')
        self.LongMarginRatioByMoney = unpacks[3]
        self.LongMarginRatioByVolume = unpacks[4]
        self.ShortMarginRatioByMoney = unpacks[5]
        self.ShortMarginRatioByVolume = unpacks[6]
        self.IsRelative = unpacks[7]

    @staticmethod
    def total_length():
        return 52

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcQryInstrumentCommissionRateField(object):
    """客户手续费查询"""
    def __init__(self):
        self.InstrumentID = ""  # 合约代码, char[13]
        self.InvestorID = 0  # 投资者代码, int32_t

    def pack(self):
        return struct.pack('=13si', self.InstrumentID.encode('utf-8'), 
                           self.InvestorID)

    def unpack(self, msg):
        unpacks = struct.unpack('=13si', msg)
        self.InstrumentID = unpacks[0].decode('utf-8').rstrip('\0')
        self.InvestorID = unpacks[1]

    @staticmethod
    def total_length():
        return 17

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcRspInstrumentCommissionRateField(object):
    """客户手续费查询回报"""
    def __init__(self):
        self.InstrumentID = ""  # 合约代码, char[13]
        self.InvestorID = 0  # 投资者代码, int32_t
        self.OpenRatioByMoney = 0  # 开仓手续费率, double
        self.OpenRatioByVolume = 0  # 开仓手续费, double
        self.CloseRatioByMoney = 0  # 平仓手续费率, double
        self.CloseRatioByVolume = 0  # 平仓手续费, double
        self.CloseTodayRatioByMoney = 0  # 平今手续费率, double
        self.CloseTodayRatioByVolume = 0  # 平今手续费, double

    def pack(self):
        return struct.pack('=13sidddddd', self.InstrumentID.encode('utf-8'), 
                           self.InvestorID, 
                           self.OpenRatioByMoney, 
                           self.OpenRatioByVolume, 
                           self.CloseRatioByMoney, 
                           self.CloseRatioByVolume, 
                           self.CloseTodayRatioByMoney, 
                           self.CloseTodayRatioByVolume)

    def unpack(self, msg):
        unpacks = struct.unpack('=13sidddddd', msg)
        self.InstrumentID = unpacks[0].decode('utf-8').rstrip('\0')
        self.InvestorID = unpacks[1]
        self.OpenRatioByMoney = unpacks[2]
        self.OpenRatioByVolume = unpacks[3]
        self.CloseRatioByMoney = unpacks[4]
        self.CloseRatioByVolume = unpacks[5]
        self.CloseTodayRatioByMoney = unpacks[6]
        self.CloseTodayRatioByVolume = unpacks[7]

    @staticmethod
    def total_length():
        return 65

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcQryInstrumentPriceField(object):
    """合约价格查询请求"""
    def __init__(self):
        self.ProductID = ""  # 产品代码, char[9]
        self.InstrumentID = ""  # 合约代码, char[13]

    def pack(self):
        return struct.pack('=9s13s', self.ProductID.encode('utf-8'), 
                           self.InstrumentID.encode('utf-8'))

    def unpack(self, msg):
        unpacks = struct.unpack('=9s13s', msg)
        self.ProductID = unpacks[0].decode('utf-8').rstrip('\0')
        self.InstrumentID = unpacks[1].decode('utf-8').rstrip('\0')

    @staticmethod
    def total_length():
        return 22

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcRspInstrumentPriceField(object):
    """合约价格查询回报"""
    def __init__(self):
        self.InstrumentID = ""  # 合约代码, char[13]
        self.UpperLimitPrice = 0  # 涨停价, double
        self.LowerLimitPrice = 0  # 跌停价, double

    def pack(self):
        return struct.pack('=13sdd', self.InstrumentID.encode('utf-8'), 
                           self.UpperLimitPrice, 
                           self.LowerLimitPrice)

    def unpack(self, msg):
        unpacks = struct.unpack('=13sdd', msg)
        self.InstrumentID = unpacks[0].decode('utf-8').rstrip('\0')
        self.UpperLimitPrice = unpacks[1]
        self.LowerLimitPrice = unpacks[2]

    @staticmethod
    def total_length():
        return 29

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcInternalVersionIdentifyField(object):
    """Internal version identify field"""
    def __init__(self):
        self.VersionInfo = 0  # Version information, int32_t

    def pack(self):
        return struct.pack('=i', self.VersionInfo)

    def unpack(self, msg):
        unpacks = struct.unpack('=i', msg)
        self.VersionInfo = unpacks[0]

    @staticmethod
    def total_length():
        return 4

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcExchangeIdentifyField(object):
    """Exchange Identify field"""
    def __init__(self):
        self.ExchangeInfo = 0  # Version information, int32_t

    def pack(self):
        return struct.pack('=i', self.ExchangeInfo)

    def unpack(self, msg):
        unpacks = struct.unpack('=i', msg)
        self.ExchangeInfo = unpacks[0]

    @staticmethod
    def total_length():
        return 4

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcRspExchangeFrontField(object):
    """交易所交易前置代码查询"""
    def __init__(self):
        self.ExchangeID = 0  # 交易所标志 0:NULL, 1:SHFE, 2:INE, 3:DCE, 4:CZCE, 5:CFFEX, int32_t
        self.FrontCount = 0  # 交易前置数量, int16_t
        self.FrontList = ""  # 交易前置代码列表, char[16]

    def pack(self):
        return struct.pack('=ih16s', self.ExchangeID, 
                           self.FrontCount, 
                           self.FrontList.encode('utf-8'))

    def unpack(self, msg):
        unpacks = struct.unpack('=ih16s', msg)
        self.ExchangeID = unpacks[0]
        self.FrontCount = unpacks[1]
        self.FrontList = unpacks[2].decode('utf-8').rstrip('\0')

    @staticmethod
    def total_length():
        return 22

    def __str__(self):
        return json.dumps(self.__dict__)


class CPhxFtdcGameStatusField(object):
    """比赛状态信息推送"""
    def __init__(self):
        self.GameStatus = 0  # 比赛状态, int32_t
        self.GameCycleID = 0  # 比赛周期编号, int32_t
        self.CurrGameCycleLeftTime = 0  # 当前比赛周期剩余时间，单位：秒, int32_t

    def pack(self):
        return struct.pack('=iii', self.GameStatus, 
                           self.GameCycleID, 
                           self.CurrGameCycleLeftTime)

    def unpack(self, msg):
        unpacks = struct.unpack('=iii', msg)
        self.GameStatus = unpacks[0]
        self.GameCycleID = unpacks[1]
        self.CurrGameCycleLeftTime = unpacks[2]

    @staticmethod
    def total_length():
        return 12

    def __str__(self):
        return json.dumps(self.__dict__)



