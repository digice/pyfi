#!/usr/bin/env python

import os
import json
import pyfwk
import pyfi

fm = pyfwk.FileManager.instance()
fm.set_root(os.path.dirname(os.path.dirname(__file__)))

session = pyfi.Session(2015, 6, 1)
print(json.dumps(session.dict(), indent=4, sort_keys=True, separators=(',', ': ')))