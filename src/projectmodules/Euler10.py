#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="rog"
__date__ ="$29-Jul-2010 12:44:04$"
import random
import sys
sys.path.append("../")
from rogutil import *
## {{{ http://code.activestate.com/recipes/366178/ (r5)



def main():
    results = []
    step = 5000
    for item in gen_primes():
        progress = len(results)
        if progress == step:
            print(len(results))
            step += 5000
        if item >= 2000000:
            break
        results.append(item)
    print ("Summing...")
    print (sum(results))

if __name__ == "__main__":
    main()
