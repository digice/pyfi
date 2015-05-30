#!/usr/bin/env python

import os
import sqlite3
import pyfwk


# ----------------------------ENTITY-DATABASE----------------------------#
class CalendarDB(pyfwk.DBase):
    dbase = None
    conn = None
    curs = None

    @staticmethod
    def instance():
        if not CalendarDB.dbase:
            CalendarDB.dbase = CalendarDB()
        return CalendarDB.dbase

    def __init__(self):
        fm = pyfwk.FileManager.instance()
        db_path = os.path.join(fm.db_dir(), 'calendar.db')
        if not os.path.exists(db_path):
            pass
        self.conn = sqlite3.connect(db_path)
        self.curs = self.conn.cursor()


# ----------------------------------MAIN----------------------------------#
def main():
    fm = pyfwk.FileManager.instance()
    fm.set_root(os.path.dirname(os.path.dirname(__file__)))
    db = CalendarDB.instance()


if __name__ == '__main__':
    main()
