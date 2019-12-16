# Q&A

### 0. 程序跑不通/报错

   请先检查是否更新了最新的demo

### 1. 如何获取并维护仓位

   OrderManager的longSnapshot和shortSnapshot为多头快照和空头快照，里面可获取多/空头Position信息及订单统计量信息。程序运行时会通过回报函数来维护OrderManager。
Demo程序重启的时候会通过ReqQryOrder和ReqQryTrade两个请求接口查询订单和成交来请求下单和成交信息，并通过OnRspQryOrder及OnRspQryTrade两个回报接口重建OrderManager。

### 2. 如何获取Instrument信息

   Demo中程序启动时调用了ReqQryInstrument接口，其回报接口OnRspQryInstrument包含了Instrument信息。

### 3. 如何查看自己Account的信息

   Demo程序中的background线程调用了ReqQryTradingAccount接口，其回报接口OnRspQryTradingAccount可获取Account信息。

### 4. 行情多久推送一次

   MarketData为切片行情，没有逐笔下单/成交行情，切片间隔为500ms，如果切片有更新会通过OnRtnMarketData推送，期权合约如果切片和上一个切片一样则不推送。

### 5. 行情中的ExchangeTime为何为0，如何获取结算时间

   ExchangeTime字段不更新，请使用game_status中的CurrGameCycleLeftTime。OnRtnGameStatus将会推送最新的比赛状态（如有更新）。

### 6. 如何遍历某个合约的订单

   OrderManager中提供了get_untraded_orders，get_unknown_orders和get_live_orders三个方法，如有其它需求可以自己定义新方法。

### 7. OrderStatus为Unknown的含义

   订单发出，但是还未收到交易所的回报

### 8. 下单报错仓位不足

   平仓时可平的仓位不足，OrderManager中get_long_position_closeable和get_short_position_closeable方法可以计算多头可平量和空头可平量。
   
### 9. 客户端初始化失败

- 检查所连接的服务端IP、端口是否正确
- 服务端每两小时整点重置服务，大概需要2分多钟时间，另外服务端每隔15分钟结算一次，结算期间也可能登录异常。如果遇到连接不上，请稍候2分钟再试试。
- 检查返回的错误日志提示，如果提示“用户已在另一个地方登录”，请确保队友没有同时登录该账号。账号同一时间只能一个人登录。

### 10. 关于游戏状态

- 只能在游戏正在运行（GameStatus=1）的时候进行下单
- 当收到游戏结算已完成的通知时（GameStatus=3），服务端已经清掉本轮的所有单子，请同步清掉本地的单子。
