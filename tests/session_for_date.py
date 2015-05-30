#!/usr/bin/env python

import os
import json
import pyfwk
import pyfi

fm = pyfwk.FileManager.instance()
fm.set_root(os.path.dirname(os.path.dirname(__file__)))

"""
If the var/db directory containing the database does not exist, the first time
the following statement is run, the calendar module will attempt to create the
sqlite database and populate with tables. Your project directory will need to be
writeable for this to occur. Also, be patient. It takes a 60-90 seconds.
"""

calendar = pyfi.Calendar(2015, 6, 1)
print(json.dumps(calendar.dict(), indent=4, sort_keys=True, separators=(',', ': ')))