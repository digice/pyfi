#!/usr/bin/env python

import pyfwk
from pyfi.entity.entity.db import EntityDB

# -----------------------------SECTOR-MODEL-----------------------------#
class SectorModel(pyfwk.Model):
    model = None
    dbase = None
    table = None
    columns = None

    @staticmethod
    def instance():
        if not SectorModel.model:
            SectorModel.model = SectorModel()
        return SectorModel.model

    def __init__(self):
        self.dbase = EntityDB.instance()
        self.table = 'sector'
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
