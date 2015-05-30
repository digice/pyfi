#!/usr/bin/env python

import pyfwk
from pyfi.calendar.calendar.db import CalendarDB

# -----------------------------CATEGORY-MODEL-----------------------------#
class SessionModel(pyfwk.Model):
    model = None
    dbase = None
    table = None
    columns = None

    @staticmethod
    def instance():
        if not SessionModel.model:
            SessionModel.model = SessionModel()
        return SessionModel.model

    def __init__(self):
        self.dbase = CalendarDB.instance()
        self.table = 'session'
        id = pyfwk.DBCol('id', 'INTEGER PRIMARY KEY')
        year = pyfwk.DBCol('year', 'INTEGER')
        month = pyfwk.DBCol('month', 'INTEGER')
        day = pyfwk.DBCol('day', 'INTEGER')
        weekday = pyfwk.DBCol('weekday', 'INTEGER')
        calendar = pyfwk.DBCol('calendar', 'INTEGER')
        self.columns = [id, year, month, day, weekday, calendar]
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
