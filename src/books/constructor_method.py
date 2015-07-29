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

#Simple Critter
#Demonstrates a basic class and object

class Critter(object):
    ''' a virtual pet'''
    def_init_(self):
        print("A new Critter has been born!")

    def talk(self):
        print("\nHi, I'm an instance of class Critter.")

#main
crit1 = Critter()
crit2 = Critter()

crit1.talk()
crit2.talk()

input("\n\nPress the enter key to exit."
)
if __name__ == '__main__':
    main()
