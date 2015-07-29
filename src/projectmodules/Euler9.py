#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="rog"
__date__ ="$29-Jul-2010 12:44:04$"
import random

def main():
    result = 0
    high = 500
    low = 1
    while result != 1000:
        xxx = []
        for i in range (3):
            xxx.append(random.randrange(low, high))
        result = xxx[0] + xxx[1] + xxx[2]
    print ("output = ", result, xxx)
if __name__ == "__main__":
    main()
