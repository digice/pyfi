#!/usr/bin/env python

import os
import sqlite3
import pyfwk


# ----------------------------ENTITY-DATABASE----------------------------#
class EntityDB(pyfwk.DBase):
    dbase = None
    conn = None
    curs = None

    @staticmethod
    def instance():
        if not EntityDB.dbase:
            EntityDB.dbase = EntityDB()
        return EntityDB.dbase

    def __init__(self):
        fm = pyfwk.FileManager.instance()
        db_path = os.path.join(fm.db_dir(), 'entity.db')
        if not os.path.exists(db_path):
            pass
            # Install()
        self.conn = sqlite3.connect(db_path)
        self.curs = self.conn.cursor()


# ----------------------------------MAIN----------------------------------#
def main():
    fm = pyfwk.FileManager.instance()
    fm.set_root(os.path.dirname(os.path.dirname(__file__)))
    db = EntityDB.instance()


if __name__ == '__main__':
    main()
