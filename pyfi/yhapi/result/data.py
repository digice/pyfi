#!/usr/bin/env python

import urllib2
import json


# ------------------------------RESULT-DATA-------------------------------#
class ResultData:
    results = None

    def __init__(self, symbol):
        url = 'http://query.yahooapis.com/v1/public/yql?q='
        url += 'select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22'
        url += str(symbol)
        url += '%22)&env=store://datatables.org/alltableswithkeys&format=json'
        web = urllib2.urlopen(url)
        if (web.getcode() == 200):
            data = json.loads(web.read())
            self.results = data['query']['results']['quote']
