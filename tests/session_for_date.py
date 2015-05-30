#!/usr/bin/env python

import os
import json
import pyfwk
import pyfi

fm = pyfwk.FileManager.instance()
fm.set_root(os.path.dirname(os.path.dirname(__file__)))

"""
The first time the following statement is run, the calendar module will attempt to
create the sqlite database and populate with tables. Your project directory will
need to be writeable for this to occur. Please be patient.
"""

# first a calendar is called, since session does not contain all dates
calendar = pyfi.Calendar(2015, 6, 1)

# need to catch errors here because possible nonsense could be passed here
if (calendar is not None):
    # now we can use what we get back from calendar to get the session by id
    session = pyfi.Session(calendar.session)
    print(json.dumps(session.dict(), indent=4, sort_keys=True, separators=(',', ': ')))
else:
    print(json.dumps({'error': 'Calendar date out of range'}))
