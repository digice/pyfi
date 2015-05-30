#!/usr/bin/env python

import pyfwk
from pyfi.entity.indices.model import IndicesModel


# -----------------------------INDICES-OBJECT-----------------------------#
class Indices(pyfwk.Object):
    id = None
    symbol = None
    name = None

    def __init__(self, id):
        self.id = id
        model = IndicesModel.instance()
        rec = model.get_rec_from_id(id)
        self.symbol = rec['symbol']
        self.name = rec['name']


# ----------------------------------MAIN----------------------------------#
def main():
    pass

if __name__ == '__main__':
    main()
