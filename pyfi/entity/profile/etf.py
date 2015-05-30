#!/usr/bin/env python

import pyfwk
from pyfi.entity.habtm.entityfund import EntityFund
from pyfi.entity.category.object import Category
from pyfi.entity.fundfamily.object import FundFamily


# ------------------------------ETF-PROFILE-------------------------------#
class ETFProfile(pyfwk.Object):
    entity = None
    category = None
    fundfamily = None

    def __init__(self, entity_id):
        self.entity = entity_id
        # check for an entry in entityfund
        efm = EntityFund.instance()
        efr = efm.get_rec_from_entity_id(entity_id)
        if (efr is not None):
            # create objects for category and fundfamily
            self.category = Category(efr['category'])
            self.fundfamily = FundFamily(efr['fundfamily'])


# ----------------------------------MAIN----------------------------------#
def main():
    pass

if __name__ == '__main__':
    main()
