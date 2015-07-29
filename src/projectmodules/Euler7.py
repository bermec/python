#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

#__author__="rog"
#__date__ ="$28-Jul-2010 14:16:47$"
import sys
sys.path.append("../")
from rogutil import *
def main():
    n = 2
    x = 0
    ans = 0

    if n == 2:
        ans = ans +1

    while ans <= 10001:
            if ans >= 10001:
                n = n - 1
                print("10001th Prime = ", n)
                exit()
            if iseven(n):
                n = n +1

            result = isprime(n)
            if result:
                ans = ans + 1
                n = n + 1
                z = iseven(n)
            else:
                n = n + 1

               # while True:
                   # ans += 1
                   # if ans == 10:
                       # print " Prime = ", n, ans
                       # break
    print("Nth Prime = ", n)



if __name__ == '__main__':
    main()
