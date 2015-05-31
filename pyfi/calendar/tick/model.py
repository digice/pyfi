#!/usr/bin/env python

import pyfwk
from pyfi.calendar.calendar.db import CalendarDB


# ------------------------------TICK-MODEL-------------------------------#
class TickModel(pyfwk.Model):
    model = None
    dbase = None
    table = None
    columns = None

    @staticmethod
    def instance():
        if not TickModel.model:
            TickModel.model = TickModel()
        return TickModel.model

    def __init__(self):
        self.dbase = CalendarDB.instance()
        self.table = 'tick'
        id = pyfwk.DBCol('id', 'INTEGER PRIMARY KEY')
        iso = pyfwk.DBCol('iso', 'INTEGER')
        hour = pyfwk.DBCol('hour', 'INTEGER')
        period = pyfwk.DBCol('period', 'INTEGER')
        minute = pyfwk.DBCol('minute', 'INTEGER')
        self.columns = [id, iso, hour, period, minute]
        self.validate()

    def get_rec_from_time(self, hour, period, minute):
        sql = 'SELECT * FROM {} WHERE hour = ? AND period = ? AND minute = ?'.format(self.table)
        rec = self.dbase.fetch_rec(sql, hour, period, minute)
        if (rec is not None):
            return rec
        else:
            raise ValueError('Time out of range')


# ----------------------------------MAIN----------------------------------#
def main():
    pass


if __name__ == '__main__':
    main()
