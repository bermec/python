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
import pdb; pdb.set_trace()

def main():
    pass


def find_details(0):
    surfers_f = open("surfing_data.csv")
    for each_line in surfers_f:
        s = {}
        (s["ID"],s["name"],s["country"],s["average"],s["board"],s["age"]) = line.split(";")
        if id2find == int(s["id"]):
            surfers_f.close()
            return (s)
    surfers_f.close()
    return({})

print("ID:         " + s["id"])
print("Name:       " + s["name"])
print("Country:    " + s["country"])
print("Average:    " + s["average"])
print("Board:      " + s["board"])
print("Age:        " + s["age"])

if __name__ == '__main__':
    main()
