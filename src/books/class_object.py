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
    def talk(self):        #Object
        print("Hi I'm an instance of class Critter.")
        crit.talk()        #Method
        input("\n\nPress the enter key to exit.")

if __name__ == '__main__':
    main()
