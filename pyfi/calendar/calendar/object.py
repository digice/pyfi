#!/usr/bin/env python

import pyfwk
from pyfi.calendar.calendar.model import CalendarModel


# ----------------------------CATEGORY-OBJECT-----------------------------#
class Calendar(pyfwk.Object):
    id = None
    year = None
    month = None
    day = None
    weekday = None
    session = None
    mktopen = None

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        model = CalendarModel.instance()
        rec = model.get_rec_from_date(year, month, day)
        self.id = rec[0]
        self.weekday = rec[4]
        self.session = rec[5]
        self.mktopen = rec[6]


# ----------------------------------MAIN----------------------------------#
def main():
    pass

if __name__ == '__main__':
    main()
