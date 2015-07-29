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
#import sys
#sys.path.append("../")
#from rogutil import *
#import pdb; pdb.set_trace()

def main():
    pass

line = "101;Jonny 'Wave Boy' Jones;USA;8.32;Fish;21"
s = {}
(s["id"],s["name"],s["country"],s["average"],s["board"],s["age"]) = line.split(";")


print("ID:         " + s["id"])
print("Name:       " + s["name"])
print("Country:    " + s["country"])
print("Average:    " + s["average"])
print("Board:      " + s["board"])
print("Age:        " + s["age"])

if __name__ == '__main__':
    main()
