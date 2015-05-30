#!/usr/bin/env python

import pyfwk
from pyfi.yhapi.result.data import ResultData
from pyfi.yhapi.averages.object import Averages
from pyfi.yhapi.dividend.object import Dividend
from pyfi.yhapi.fundamentals.object import Fundamentals
from pyfi.yhapi.quote.object import Quote
from pyfi.yhapi.range.object import Range


# -----------------------------RESULT-OBJECT------------------------------#
class Result(pyfwk.Object):
    averages = None
    dividend = None
    fundamentals = None
    quote = None
    range = None

    def __init__(self, symbol):
        data = ResultData(symbol)
        self.averages = Averages(data.results)
        self.dividend = Dividend(data.results)
        self.fundamentals = Fundamentals(data.results)
        self.quote = Quote(data.results)
        self.range = Range(data.results)


__all__ = ['Result']
