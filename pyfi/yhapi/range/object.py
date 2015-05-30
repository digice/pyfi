#!/usr/env/python

import pyfwk


# ------------------------------RANGE-OBJECT------------------------------#
class Range(pyfwk.Object):
    daylow = None
    dayhigh = None
    yearlow = None
    yearhigh = None
    changefromyearlow = None
    pctchangefromyearlow = None
    changefromyearhigh = None
    pctchangefromyearhigh = None
    dayrange = None
    yearrange = None

    def __init__(self, data):
        if (data['DaysLow'] is not None):
            self.daylow = data['DaysLow']
        if (data['DaysHigh'] is not None):
            self.dayhigh = data['DaysHigh']
        if (data['YearLow'] is not None):
            self.yearlow = data['YearLow']
        if (data['YearHigh'] is not None):
            self.yearhigh = data['YearHigh']
        if (data['ChangeFromYearLow'] is not None):
            self.changefromyearlow = data['ChangeFromYearLow']
        if (data['PercentChangeFromYearLow'] is not None):
            self.pctchangefromyearlow = data['PercentChangeFromYearLow']
        if (data['ChangeFromYearHigh'] is not None):
            self.changefromyearhigh = data['ChangeFromYearHigh']
        if (data['PercebtChangeFromYearHigh'] is not None):
            self.pctchangefromyearhigh = data['PercebtChangeFromYearHigh']
        if (data['DaysRange'] is not None):
            self.dayrange = data['DaysRange']
        if (data['YearRange'] is not None):
            self.yearrange = data['YearRange']
