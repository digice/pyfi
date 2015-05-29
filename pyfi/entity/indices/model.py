#!/usr/bin/env python

import pyfwk
from pyfi.entity.entity.db import EntityDB

# ------------------------------INDICES-MODEL-----------------------------#
class IndicesModel(pyfwk.Model):
    model = None
    dbase = None
    table = None
    columns = None

    @staticmethod
    def instance():
        if not IndicesModel.model:
            IndicesModel.model = IndicesModel()
        return IndicesModel.model

    def __init__(self):
        self.dbase = EntityDB.instance()
        self.table = 'indices'
        id = pyfwk.DBCol('id', 'INTEGER PRIMARY KEY')
        symbol = pyfwk.DBCol('symbol', 'TEXT')
        name = pyfwk.DBCol('name', 'TEXT')
        self.columns = [id, symbol, name]
        self.validate()


# ----------------------------------MAIN----------------------------------#
def main():
    pass


if __name__ == '__main__':
    main()
