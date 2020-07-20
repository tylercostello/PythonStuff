import talib
import numpy as np
import math
def initialize(context):
    set_slippage()
    context.max_notional = 100000
    context.SPXL = sid(37514)  # SPXL
    context.SPXS = sid(37083)  # SPXL
    context.LOW_MOMENTUM = -11
    context.HIGH_MOMENTUM = -11
    schedule_function(rebalance, date_rules.every_day(), time_rules.market_open())
def rebalance(context, data):
    prices = data.history(context.SPXL, 'price', 15, '1d')
    shortprices = data.history(context.SPXS, 'price', 15, '1d')
    mlist=talib.MOM(prices, timeperiod=12)[-1]
    positions = context.portfolio.positions
    if mlist < context.LOW_MOMENTUM and context.SPXL in positions:
        order_target(context.SPXL, 0)
    elif mlist > context.HIGH_MOMENTUM and context.SPXL not in positions:
        order_target_value(context.SPXL, context.max_notional)
    record(SPXLM=mlist)
