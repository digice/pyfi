#!/usr/bin/env python


# ---------------------------INDICES-MEMBERSHIP----------------------------#
class IndicesMembership:
    """
      override dict method to provide a list of indices
    """
    lst = None

    def __init__(self, lst):
        self.lst = lst

    def dict(self):
        lst = []
        for obj in self.lst:
            lst.append(obj.dict())
        return lst


# ----------------------------------MAIN----------------------------------#
def main():
    pass


if __name__ == '__main__':
    main()
