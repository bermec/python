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



# Attribute Critter
# Demonstrates creating and accessing object attributes

class Critter(object):
    """A virtual pet"""
    """Creates a class attribute total"""
    total = 0

    '''static method'''
    @staticmethod
    def status():
        print("\nThe total number of critters is ", Critter.total)

    '''constructor method'''
    def __init__(self, name):
        print("A Critter has been born!")
        self.name = name
        Critter.total += 1

#main
print("Accessing the class attribute Critter.total:", end=" ")
print(Critter.total)

print("\nCreating Critters.")
crit1 = Critter("Critter 1")
crit2 = Critter("Critter 2")
crit3 = Critter("Critter 3")

'''Invoking static method'''
Critter.status()

print("\nAccessing the class attribute through an object:", end= " ")
print(crit1.total)

input("\n\nPress the enter key to exit.")