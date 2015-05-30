#!/usr/env/python

import pyfwk


# ------------------------------QUOTE-OBJECT------------------------------#
class Quote(pyfwk.Object):
    ask = None
    bid = None
    change = None
    tradedate = None
    lasttrade = None
    open = None
    prevclose = None
    tradetime = None
    volume = None
    daychange = None
    pctchange = None

    def __init__(self, data):
        if (data['Ask'] is not None):
            self.ask = data['Ask']
        if (data['Bid'] is not None):
            self.bid = data['Bid']
        if (data['Change'] is not None):
            self.change = data['Change']
        if (data['LastTradeDate'] is not None):
            self.tradedate = data['LastTradeDate']
        if (data['LastTradePriceOnly'] is not None):
            self.lasttrade = data['LastTradePriceOnly']
        if (data['Open'] is not None):
            self.open = data['Open']
        if (data['PreviousClose'] is not None):
            self.prevclose = data['PreviousClose']
        if (data['LastTradeTime'] is not None):
            self.tradetime = data['LastTradeTime']
        if (data['Volume'] is not None):
            self.volume = data['Volume']
        if (data['DaysValueChange'] is not None):
            self.daychange = data['DaysValueChange']
        if (data['PercentChange'] is not None):
            self.pctchange = data['PercentChange']
