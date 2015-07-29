#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="rog"
__date__ ="$29-Jul-2010 12:44:04$"
#from rogutil import *
# Check for first Triangle Number to have more than 500 divisors.

def main():
    n = 501
    count = 0
    zzz = n - 1

    while count != 500:


        zzz = zzz - 1
        if n % zzz == 0:
            count = count + 1
            zzz = zzz- 1
        if count == 500:
                print ("working!  ",n," count = ",count)
                exit()
        if zzz == 1:
            n = n + 1



if __name__ == "__main__":
    main()
