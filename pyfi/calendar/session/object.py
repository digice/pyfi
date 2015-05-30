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

    def __init__(self, id):
        self.id = id
        model = SessionModel.instance()
        rec = model.get_rec_from_id(id)
        self.year = rec['year']
        self.month = rec['month']
        self.day = rec['day']
        self.weekday = rec['weekday']
        self.calendar = rec['calendar']


# ----------------------------------MAIN----------------------------------#
def main():
    pass

if __name__ == '__main__':
    main()
