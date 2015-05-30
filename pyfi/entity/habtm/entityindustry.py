#!/usr/bin/env python

import os
import pyfwk

from pyfi.entity.entity.db import EntityDB


# -----------------------------ENTITY-INDUSTRY----------------------------#
class EntityIndustry(pyfwk.Model):
    model = None
    dbase = None
    table = None
    columns = None

    @staticmethod
    def instance():
        if not EntityIndustry.model:
            EntityIndustry.model = EntityIndustry()
        return EntityIndustry.model

    def __init__(self):
        self.dbase = EntityDB.instance()
        self.table = 'entityindustry'
        id = pyfwk.DBCol('id', 'INTEGER PRIMARY KEY')
        entity = pyfwk.DBCol('entity', 'INTEGER')
        industry = pyfwk.DBCol('industry', 'INTEGER')
        self.columns = [id, entity, industry]
        self.validate()


# ----------------------------------MAIN----------------------------------#
def main():
    fm = pyfwk.FileManager.instance()
    fm.set_root(os.path.dirname(os.path.dirname(__file__)))
    ei = EntityIndustry.instance()

if __name__ == '__main__':
    main()
