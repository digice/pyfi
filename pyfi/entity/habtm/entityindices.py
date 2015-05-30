#!/usr/bin/env python

import os
import pyfwk

from pyfi.entity.entity.db import EntityDB


# -----------------------------ENTITY-INDUSTRY----------------------------#
class EntityIndices(pyfwk.Model):
    model = None
    dbase = None
    table = None
    columns = None

    @staticmethod
    def instance():
        if not EntityIndices.model:
            EntityIndices.model = EntityIndices()
        return EntityIndices.model

    def __init__(self):
        self.dbase = EntityDB.instance()
        self.table = 'entityindices'
        id = pyfwk.DBCol('id', 'INTEGER PRIMARY KEY')
        entity = pyfwk.DBCol('entity', 'INTEGER')
        indices = pyfwk.DBCol('indices', 'INTEGER')
        self.columns = [id, entity, indices]
        self.validate()


# ----------------------------------MAIN----------------------------------#
def main():
    fm = pyfwk.FileManager.instance()
    fm.set_root(os.path.dirname(os.path.dirname(__file__)))
    ei = EntityIndices.instance()

if __name__ == '__main__':
    main()
