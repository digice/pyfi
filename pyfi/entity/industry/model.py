#!/usr/bin/env python

import pyfwk
from pyfi.entity.entity.db import EntityDB

# -----------------------------INDUSTRY-MODEL-----------------------------#
class IndustryModel(pyfwk.Model):
    model = None
    dbase = None
    table = None
    columns = None

    @staticmethod
    def instance():
        if not IndustryModel.model:
            IndustryModel.model = IndustryModel()
        return IndustryModel.model

    def __init__(self):
        self.dbase = EntityDB.instance()
        self.table = 'industry'
        id = pyfwk.DBCol('id', 'INTEGER PRIMARY KEY')
        sector = pyfwk.DBCol('sector', 'INTEGER')
        name = pyfwk.DBCol('name', 'TEXT')
        self.columns = [id, sector, name]
        self.validate()


# ----------------------------------MAIN----------------------------------#
def main():
    pass


if __name__ == '__main__':
    main()
