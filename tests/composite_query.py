#!/usr/bin/env python

import os
import json
import pyfwk
import pyfi

fm = pyfwk.FileManager.instance()
fm.set_root(os.path.dirname(os.path.dirname(__file__)))

"""
Run this test last.
In this example, if an object is null, it is simply omitted from the json return.
If you want to be sure you get a dictionary key for each, add an else clause to
the conditional to return the key with a null value or 'Not Found' indication.
"""

# initialize the final dictionary to output
dct = {}
# create the entity object, which will contain the symbol needed for results
entity = pyfi.Entity(1000)
if (entity is not None):
    dct['entity'] = entity.dict()
    # create the result object
    result = pyfi.Result(entity.symbol)
    if (result is not None):
        dct['yhapi'] = result.dict()
        # find the last trade date
        date = result.quote.tradedate
        dar = str(date).split('/')
        month = dar[0]
        day = dar[1]
        year = dar[2]
        calendar = pyfi.Calendar(year, month, day)
        if (calendar is not None):
            session = pyfi.Session(calendar.session)
            if (session is not None):
                dct['session'] = session.dict()
else:
    dct = {'error': 'ID was not recognized'}

print(json.dumps(dct, indent=4, sort_keys=True, separators=(',', ': ')))
