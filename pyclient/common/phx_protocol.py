import struct


class CPhxFtdcHeader(object):
    def __init__(self):
        self.Version = 0    # 协议版本号, uint8_t
        self.Type = 0    # FTDC报文类型，详见FTDC报文类型定义, uint8_t
        self.Chain = 0    # 报文链，详见FTDC报文链类型定义, uint8_t
        self.Reserved0 = 0    # 保留字段（补齐）, uint8_t
        self.TransactionID = 0    # 报文业务类型，详见FTDC业务类型定义, uint16_t
        self.SequenceSeries = 0    # 序列系列号, uint16_t
        self.SequenceNumber = 0    # 序列号, uint32_t
        self.ContentLength = 0    # 信息正文长度, uint16_t

    def pack(self):
        return struct.pack(
            '=BBBBHHIH', self.Version, self.Type, self.Chain, self.Reserved0, self.TransactionID, self.SequenceSeries,
            self.SequenceNumber, self.ContentLength
        )

    def unpack(self, msg):
        self.Version, \
            self.Type, \
            self.Chain, \
            self.Reserved0, \
            self.TransactionID, \
            self.SequenceSeries, \
            self.SequenceNumber, \
            self.ContentLength = struct.unpack('=BBBBHHIH', msg)

    @staticmethod
    def total_length():
        return 14


class CPhxFtdcPackage(object):
    def __init__(self):
        self.Version = 0    # 协议版本号, uint8_t
        self.Type = 0    # FTDC报文类型，详见FTDC报文类型定义, uint8_t
        self.Chain = 0    # 报文链，详见FTDC报文链类型定义, uint8_t
        self.Reserved0 = 0    # 保留字段（补齐）, uint8_t
        self.TransactionID = 0    # 报文业务类型，详见FTDC业务类型定义, uint16_t
        self.SequenceSeries = 0    # 序列系列号, uint16_t
        self.SequenceNumber = 0    # 序列号, uint32_t
        self.ContentLength = 0    # 信息正文长度, uint16_t

    def pack(self):
        return struct.pack(
            '=BBBBHHIH', self.Version, self.Type, self.Chain, self.Reserved0, self.TransactionID, self.SequenceSeries,
            self.SequenceNumber, self.ContentLength
        )

    def unpack(self, msg):
        self.Version, \
            self.Type, \
            self.Chain, \
            self.Reserved0, \
            self.TransactionID, \
            self.SequenceSeries, \
            self.SequenceNumber, \
            self.ContentLength = struct.unpack('=BBBBHHIH', msg)

    @staticmethod
    def total_length():
        return 14


class CPhxFtdcReqPackage(object):
    def __init__(self):
        self.Version = 0    # 协议版本号, uint8_t
        self.Type = 0    # FTDC报文类型，详见FTDC报文类型定义, uint8_t
        self.Chain = 0    # 报文链，详见FTDC报文链类型定义, uint8_t
        self.Reserved0 = 0    # 保留字段（补齐）, uint8_t
        self.TransactionID = 0    # 报文业务类型，详见FTDC业务类型定义, uint16_t
        self.SequenceSeries = 0    # 序列系列号, uint16_t
        self.SequenceNumber = 0    # 序列号, uint32_t
        self.ContentLength = 0    # 信息正文长度, uint16_t
        self.RequestID = 0    # 客户请求编号, int32_t

    def pack(self):
        return struct.pack(
            '=BBBBHHIHi', self.Version, self.Type, self.Chain, self.Reserved0, self.TransactionID, self.SequenceSeries,
            self.SequenceNumber, self.ContentLength, self.RequestID
        )

    def unpack(self, msg):
        self.Version, \
            self.Type, \
            self.Chain, \
            self.Reserved0, \
            self.TransactionID, \
            self.SequenceSeries, \
            self.SequenceNumber, \
            self.ContentLength, \
            self.RequestID = struct.unpack('=BBBBHHIHi', msg)

    @staticmethod
    def total_length():
        return 18


class CPhxFtdcRspPackage(object):
    def __init__(self):
        self.Version = 0    # 协议版本号, uint8_t
        self.Type = 0    # FTDC报文类型，详见FTDC报文类型定义, uint8_t
        self.Chain = 0    # 报文链，详见FTDC报文链类型定义, uint8_t
        self.Reserved0 = 0    # 保留字段（补齐）, uint8_t
        self.TransactionID = 0    # 报文业务类型，详见FTDC业务类型定义, uint16_t
        self.SequenceSeries = 0    # 序列系列号, uint16_t
        self.SequenceNumber = 0    # 序列号, uint32_t
        self.ContentLength = 0    # 信息正文长度, uint16_t
        self.RequestID = 0    # 客户请求编号, int32_t
        self.ErrorID = 0    # 应答错误码（0 - 正常; 非0 - 错误）, int16_t

    def pack(self):
        return struct.pack(
            '=BBBBHHIHih', self.Version, self.Type, self.Chain, self.Reserved0, self.TransactionID, self.SequenceSeries,
            self.SequenceNumber, self.ContentLength, self.RequestID, self.ErrorID
        )

    def unpack(self, msg):
        self.Version, \
            self.Type, \
            self.Chain, \
            self.Reserved0, \
            self.TransactionID, \
            self.SequenceSeries, \
            self.SequenceNumber, \
            self.ContentLength, \
            self.RequestID, \
            self.ErrorID = struct.unpack('=BBBBHHIHih', msg)

    @staticmethod
    def total_length():
        return 20

