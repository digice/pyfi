#!/usr/bin/env python

import pyfwk
from pyfi.calendar.calendar.db import CalendarDB


# -----------------------------CATEGORY-MODEL-----------------------------#
class CalendarModel(pyfwk.Model):
    model = None
    dbase = None
    table = None
    columns = None

    @staticmethod
    def instance():
        if not CalendarModel.model:
            CalendarModel.model = CalendarModel()
        return CalendarModel.model

    def __init__(self):
        self.dbase = CalendarDB.instance()
        self.table = 'calendar'
        id = pyfwk.DBCol('id', 'INTEGER PRIMARY KEY')
        year = pyfwk.DBCol('year', 'INTEGER')
        month = pyfwk.DBCol('month', 'INTEGER')
        day = pyfwk.DBCol('day', 'INTEGER')
        weekday = pyfwk.DBCol('weekday', 'INTEGER')
        session = pyfwk.DBCol('session', 'INTEGER')
        mktopen = pyfwk.DBCol('mktopen', 'INTEGER')
        self.columns = [id, year, month, day, weekday, session, mktopen]
        self.validate()

    def get_rec_from_date(self, year, month, day):
        sql = 'SELECT * FROM {} WHERE year = ? AND month = ? AND day = ?'.format(self.table)
        rec = self.dbase.fetch_rec(sql, year, month, day)
        if (rec is not None):
            return rec
        else:
            raise ValueError('Date out of range')


# ----------------------------------MAIN----------------------------------#
def main():
    pass


if __name__ == '__main__':
    main()
