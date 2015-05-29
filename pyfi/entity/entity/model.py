#!/usr/bin/env python

import os
import pyfwk

from pyfi.entity.entity.db import EntityDB

# ------------------------------ENTITY-MODEL------------------------------#
class EntityModel(pyfwk.Model):
    model = None
    dbase = None
    table = None
    columns = None

    @staticmethod
    def instance():
        if not EntityModel.model:
            EntityModel.model = EntityModel()
        return EntityModel.model

    def __init__(self):
        self.dbase = EntityDB.instance()
        self.table = 'entity'
        id = pyfwk.DBCol('id', 'INTEGER PRIMARY KEY')
        symbol = pyfwk.DBCol('symbol', 'TEXT')
        name = pyfwk.DBCol('name', 'TEXT')
        type = pyfwk.DBCol('type', 'INTEGER')
        exchange = pyfwk.DBCol('exchange', 'INTEGER')
        profile = pyfwk.DBCol('profile', 'INTEGER')
        self.columns = [id, symbol, name, type, exchange, profile]
        self.validate()


# ----------------------------------MAIN----------------------------------#
def main():
    fm = pyfwk.FileManager.instance()
    fm.set_root(os.path.dirname(os.path.dirname(__file__)))
    em = EntityModel.instance()

if __name__ == '__main__':
    main()
