#!/usr/bin/env python

import os
import json
import pyfwk
import pyfi

fm = pyfwk.FileManager.instance()
fm.set_root(os.path.dirname(os.path.dirname(__file__)))

entity = pyfi.Entity(1123)
print(json.dumps(entity.dict(), indent=4, sort_keys=True, separators=(',', ': ')))