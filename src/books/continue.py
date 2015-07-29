#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      rog
#
# Created:     02/08/2010
# Copyright:   (c) rog 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys
sys.path.append("../")
from rogutil import *


def main():
    pass


    while True:
        s = (input("Enter something :"))
        if s == "quit":
            break
        if len(s) < 3:
            print("Too small")
            continue

#Continue skips any other stages in the loop and continues with
# another iteration of the loop

if __name__ == '__main__':
    main()

