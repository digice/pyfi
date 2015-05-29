#!/usr/bin/env python

import pyfwk
from pyfi.entity.industry.model import IndustryModel

# ----------------------------INDUSTRY-OBJECT-----------------------------#
class Industry(pyfwk.Object):
    id = None
    symbol = None
    name = None

    def __init__(self, id):
        self.id = id
        model = IndustryModel.instance()
        rec = model.get_rec_from_id(id)
        self.sector = rec['sector']
        self.name = rec['name']


# ----------------------------------MAIN----------------------------------#
def main():
    pass

if __name__ == '__main__':
    main()
