#!/usr/bin/env python

import pyfwk
from pyfi.entity.habtm.entityindustry import EntityIndustry
from pyfi.entity.habtm.entityindices import EntityIndices
from pyfi.entity.industry.object import Industry
from pyfi.entity.sector.object import Sector
from pyfi.entity.indices.object import Indices
from pyfi.entity.indices.membership import IndicesMembership


# -----------------------------STOCK-PROFILE------------------------------#
class StockProfile(pyfwk.Object):
    entity = None
    industry = None
    sector = None
    indices = None

    def __init__(self, entity_id):
        self.entity = entity_id
        # check for an entry in entityfund
        eim = EntityIndustry.instance()
        eir = eim.get_rec_from_entity_id(entity_id)
        if (eir is not None):
            # create objects for industry and sector
            self.industry = Industry(eir['industry'])
            self.sector = Sector(self.industry.sector)
        # check for indices membership
        exm = EntityIndices.instance()
        exs = exm.get_recs_from_entity_id(entity_id)
        if (exs is not None):
            # create the modified indices object (list of indices)
            indices = []
            for exr in exs:
                obj = Indices(exr['indices'])
                indices.append(obj)
            self.indices = IndicesMembership(indices)


# ----------------------------------MAIN----------------------------------#
def main():
    pass

if __name__ == '__main__':
    main()
