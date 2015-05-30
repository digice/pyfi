#!/usr/bin/env python

import pyfwk
from pyfi.entity.entity.db import EntityDB


# -----------------------------CATEGORY-MODEL-----------------------------#
class CategoryModel(pyfwk.Model):
    model = None
    dbase = None
    table = None
    columns = None

    @staticmethod
    def instance():
        if not CategoryModel.model:
            CategoryModel.model = CategoryModel()
        return CategoryModel.model

    def __init__(self):
        self.dbase = EntityDB.instance()
        self.table = 'category'
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
