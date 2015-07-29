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

'''Usually used to provide read-only access to a private attribute'''
def main():
    pass

class Critter(object):
    '''A virtual pet'''
    def __init__(self, name):
        print("A new critter has been born!")
        self.__name = name
        
    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("A critters namecan't be the empty string.")
        else:
            self.__name = new_name
            print("Name change successful!")
            
    def talk(self):
        print("\nHi, I'm ", self.name)
        
# main
crit = Critter("Poochie")
    
crit.talk()

print("\nMy critters name is:", end= " ")
print(crit.name)

print("\nAttempting to change my critters name to Randolph....")
crit.name = "Randolph"

print("My critters name is:", end= " ")
print(crit.name)

print("\nAttempting to change my critters name to the empty string...")
crit.name = ""


print("My critters name is:", end= " ")
print(crit.name)

input("\nPress any key to exit.")
      
if __name__ == '__main__':
    main()
