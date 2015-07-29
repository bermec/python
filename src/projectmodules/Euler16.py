#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="rog"
__date__ ="$29-Jul-2010 12:44:04$"

import sys
from rogutil import multiplylist
sys.path.append("../")
#What is the sum of the digits of the number 2^1000?

def main():
    print(sum(list(map(int, list(str(2**1000))))))

if __name__ == "__main__":
    main()
