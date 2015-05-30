#!/usr/bin/env python

import os
import pyfwk

from pyfi.entity.entity.db import EntityDB


# -------------------------------ENTITY-FUND------------------------------#
class EntityFund(pyfwk.Model):
    model = None
    dbase = None
    table = None
    columns = None

    @staticmethod
    def instance():
        if not EntityFund.model:
            EntityFund.model = EntityFund()
        return EntityFund.model

    def __init__(self):
        self.dbase = EntityDB.instance()
        self.table = 'entityfund'
        id = pyfwk.DBCol('id', 'INTEGER PRIMARY KEY')
        entity = pyfwk.DBCol('entity', 'INTEGER')
        category = pyfwk.DBCol('category', 'INTEGER')
        fundfamily = pyfwk.DBCol('fundfamily', 'INTEGER')
        self.columns = [id, entity, category, fundfamily]
        self.validate()


# ----------------------------------MAIN----------------------------------#
def main():
    fm = pyfwk.FileManager.instance()
    fm.set_root(os.path.dirname(os.path.dirname(__file__)))
    ef = EntityFund.instance()

if __name__ == '__main__':
    main()
