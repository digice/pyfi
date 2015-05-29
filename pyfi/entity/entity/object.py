#!/usr/bin/env python

import os
import pyfwk
from pyfi.entity.entity.model import EntityModel
from pyfi.entity.exchange.object import Exchange
from pyfi.entity.type.object import Type
from pyfi.entity.profile.stock import StockProfile
from pyfi.entity.profile.etf import ETFProfile

# -----------------------------ENTITY-OBJECT------------------------------#
class Entity(pyfwk.Object):
    id = None
    symbol = None
    name = None
    type = None
    exchange = None
    profile = None

    def __init__(self, id):
        self.id = id
        model = EntityModel.instance()
        rec = model.get_rec_from_id(id)
        self.symbol = rec['symbol']
        self.name = rec['name']
        self.type = Type(rec['type'])
        self.exchange = Exchange(rec['exchange'])
        self.profile = rec['profile']
        if (rec['profile'] == 1):
           if (self.type.id == 1):
               self.profile = StockProfile(self.id)
           elif (self.type.id == 2):
               self.profile = ETFProfile(self.id)


# ----------------------------------MAIN----------------------------------#
def main():
    fm = pyfwk.FileManager.instance()
    fm.set_root(os.path.dirname(os.path.dirname(__file__)))
    entity = Entity(1127)
    print(entity.dict())

if __name__ == '__main__':
    main()
