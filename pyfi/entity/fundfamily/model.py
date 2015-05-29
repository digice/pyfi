#!/usr/bin/env python

import os
import pyfwk

from pyfi.entity.entity.db import EntityDB

# ---------------------------FUND-FAMILY-MODEL---------------------------#
class FundFamilyModel(pyfwk.Model):
    model = None
    dbase = None
    table = None
    columns = None

    @staticmethod
    def instance():
        if not FundFamilyModel.model:
            FundFamilyModel.model = FundFamilyModel()
        return FundFamilyModel.model

    def __init__(self):
        self.dbase = EntityDB.instance()
        self.table = 'fundfamily'
        id = pyfwk.DBCol('id', 'INTEGER PRIMARY KEY')
        symbol = pyfwk.DBCol('symbol', 'TEXT')
        name = pyfwk.DBCol('name', 'TEXT')
        self.columns = [id, symbol, name]
        self.validate()


# ----------------------------------MAIN----------------------------------#
def main():
    fm = pyfwk.FileManager.instance()
    fm.set_root(os.path.dirname(os.path.dirname(__file__)))
    cm = FundFamilyModel.instance()

if __name__ == '__main__':
    main()
