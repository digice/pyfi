#!/usr/bin/env python

import pyfwk
from pyfi.calendar.session.model import SessionModel

# ----------------------------CATEGORY-OBJECT-----------------------------#
class Session(pyfwk.Object):
    id = None
    year = None
    month = None
    day = None
    weekday = None
    calendar = None

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        model = SessionModel.instance()
        rec = model.get_rec_from_date(year, month, day)
        self.id = rec[0]
        self.weekday = rec[4]
        self.calendar = rec[5]


# ----------------------------------MAIN----------------------------------#
def main():
    pass

if __name__ == '__main__':
    main()
