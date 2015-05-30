#!/usr/env/python

import pyfwk


# ----------------------------AVERAGES-OBJECT-----------------------------#
class Averages(pyfwk.Object):
    dailyvolume = None
    fiftyday = None
    twohundredday = None
    changefromtwohundredday = None
    pctchangefromtwohundredday = None
    changefromfiftyday = None
    pctchangefromfiftyday = None

    def __init__(self, data):
        if (data['AverageDailyVolume'] is not None):
            self.dailyvolume = data['AverageDailyVolume']
        if (data['FiftydayMovingAverage'] is not None):
            self.fiftyday = data['FiftydayMovingAverage']
        if (data['TwoHundreddayMovingAverage'] is not None):
            self.twohundredday = data['TwoHundreddayMovingAverage']
        if (data['ChangeFromTwoHundreddayMovingAverage'] is not None):
            self.changefromtwohundredday = data['ChangeFromTwoHundreddayMovingAverage']
        if (data['PercentChangeFromTwoHundreddayMovingAverage'] is not None):
            self.pctchangefromtwohundredday = data['PercentChangeFromTwoHundreddayMovingAverage']
        if (data['ChangeFromFiftydayMovingAverage'] is not None):
            self.changefromfiftyday = data['ChangeFromFiftydayMovingAverage']
        if (data['PercentChangeFromFiftydayMovingAverage'] is not None):
            self.pctchangefromfiftyday = data['PercentChangeFromFiftydayMovingAverage']
