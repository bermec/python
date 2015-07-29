#---------
# Name:        module1
# Purpose:
#
# Author:      rog
#
# Created:     04/08/2010
# Copyright:   (c) rog 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
from rogutil import *
import sys

def main():
    # ---- DEBUGGER ----

    #if len(sys.argv) > 1:
    #import pdb; pdb.set_trace()


    inventory= ["1", "4", "8"]

    for items in inventory:
        print (items)

    print("Your items are  ",len(inventory))

    if "4" in inventory:
        print("'4' IS here!!")

    mump = {"four": 4,"eight": 8}
    d = (mump.get("four"))
    print (d* d)

if __name__ == '__main__':
    main()






