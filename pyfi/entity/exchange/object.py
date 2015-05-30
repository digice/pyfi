#!/usr/bin/env python

import pyfwk
from pyfi.entity.exchange.model import ExchangeModel


# ----------------------------EXCHANGE-OBJECT-----------------------------#
class Exchange(pyfwk.Object):
    id = None
    symbol = None
    name = None

    def __init__(self, id):
        self.id = id
        model = ExchangeModel.instance()
        rec = model.get_rec_from_id(id)
        self.symbol = rec['symbol']
        self.name = rec['name']
