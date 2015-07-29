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

# Private Critter
# Demonstrates private variables and methods
class Critter(object):
    """A virtual pet"""
    def __init__(self, name, mood):
        print("A new critter has been born! ")
        self.name = name     # public attrbute
        self.__mood = mood   # private attribute
        
    '''Accessing self.mood (private)from inside the class'''    
    def talk(self):
        print("\nI'm", self.name)
        print("Right now I feel", self.__mood, "\n")


if __name__ == '__main__':
    main()
