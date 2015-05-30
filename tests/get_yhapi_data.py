#!/usr/bin/env python

import json
import pyfi

result = pyfi.Result('JPM')
print(json.dumps(result.dict(), indent=4, sort_keys=True, separators=(',', ': ')))
