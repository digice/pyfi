#!/usr/env/python

import pyfwk


# --------------------------FUNDAMENTALS-OBJECT---------------------------#
class Fundamentals(pyfwk.Object):
    bookvalue = None
    eps = None
    epsestcurrentyear = None
    epsestnextyear = None
    epsestnextqtr = None
    marketcap = None
    ebitda = None
    pricetosales = None
    pricetobook = None
    peratio = None
    pegratio = None
    pricetoepsestcurrentyear = None
    pricetoepsestnextyear = None
    shortratio = None
    oneyeartarget = None

    def __init__(self, data):
        if (data['BookValue'] is not None):
            self.bookvalue = data['BookValue']
        if (data['EarningsShare'] is not None):
            self.eps = data['EarningsShare']
        if (data['EPSEstimateCurrentYear'] is not None):
            self.epsestcurrentyear = data['EPSEstimateCurrentYear']
        if (data['EPSEstimateNextYear'] is not None):
            self.epsestnextyear = data['EPSEstimateNextYear']
        if (data['EPSEstimateNextQuarter'] is not None):
            self.epsestnextqtr = data['EPSEstimateNextQuarter']
        if (data['MarketCapitalization'] is not None):
            self.marketcap = data['MarketCapitalization']
        if (data['EBITDA'] is not None):
            self.ebitda = data['EBITDA']
        if (data['PriceSales'] is not None):
            self.pricetosales = data['PriceSales']
        if (data['PriceBook'] is not None):
            self.pricetobook = data['PriceBook']
        if (data['PERatio'] is not None):
            self.peratio = data['PERatio']
        if (data['PEGRatio'] is not None):
            self.pegratio = data['PEGRatio']
        if (data['PriceEPSEstimateCurrentYear'] is not None):
            self.pricetoepsestcurrentyear = data['PriceEPSEstimateCurrentYear']
        if (data['PriceEPSEstimateNextYear'] is not None):
            self.pricetoepsestnextyear = data['PriceEPSEstimateNextYear']
        if (data['ShortRatio'] is not None):
            self.shortratio = data['ShortRatio']
        if (data['OneyrTargetPrice'] is not None):
            self.oneyeartarget = data['OneyrTargetPrice']
