#!/usr/env/python

import pyfwk


# ----------------------------DIVIDEND-OBJECT-----------------------------#
class Dividend(pyfwk.Object):
    dividendpershare = None
    exdividenddate = None
    dividendpaydate = None
    dividendyield = None

    def __init__(self, data):
        if (data['DividendShare'] is not None):
            self.dividendpershare = data['DividendShare']
        if (data['ExDividendDate'] is not None):
            self.exdividenddate = data['ExDividendDate']
        if (data['DividendPayDate'] is not None):
            self.dividendpaydate = data['DividendPayDate']
        if (data['DividendYield'] is not None):
            self.dividendyield = data['DividendYield']
