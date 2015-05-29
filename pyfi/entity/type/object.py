#!/usr/bin/env python

import pyfwk
from pyfi.entity.type.model import TypeModel

# ----------------------------EXCHANGE-OBJECT-----------------------------#
class Type(pyfwk.Object):
    id = None
    symbol = None
    name = None

    def __init__(self, id):
        self.id = id
        model = TypeModel.instance()
        rec = model.get_rec_from_id(id)
        self.symbol = rec['symbol']
        self.name = rec['name']

