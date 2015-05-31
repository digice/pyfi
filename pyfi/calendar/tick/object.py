#!/usr/bin/env python

import pyfwk
from pyfi.calendar.tick.model import TickModel


# ----------------------------CATEGORY-OBJECT-----------------------------#
class Tick(pyfwk.Object):
    id = None
    iso = None
    hour = None
    period = None
    minute = None

    def __init__(self, hour, minute, period):
        self.hour = hour
        self.period = period
        self.minute = minute
        model = TickModel.instance()
        rec = model.get_rec_from_time(hour, period, minute)
        self.id = rec[0]
        self.iso = rec[1]


# ----------------------------------MAIN----------------------------------#
def main():
    pass

if __name__ == '__main__':
    main()
