#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rog
#
# Created:     14/10/2010
# Copyright:   (c) rog 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
'''A perfect number is a number for which the sum of its proper divisors is
 exactly equal to the number. For example, the sum of the proper divisors of
  28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
 and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers
is 24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However, this
upper limit cannot be reduced any further by analysis even though it is
known that the greatest number that cannot be expressed as the sum of
two abundant numbers is less than this limit.

Find the sum of all the positive integers which CANNOT be written
as the sum of two abundant numbers.'''
import math
import sys
sys.path.append("../")
from rogutil import *
import time
tt = time.time()

def main():
    pass
    result = 0
    count = 0
    increm = 1

    '''generator for trinum'''
    v = (x for x in range(28123, 0, -1))
    trinum = next(v)
    #trinum = 12

    kounter = 0     # errr... counter
    prim = 0        # The Prime Number for division of the Triangle number
    i, z = 0, 0
    prims = gen_x(10000, gen_primes)     # prime number genny
    prim = prims[z]                     # For incrementing the Prime Number
    div_lst = []            #Divisor list
    power_lst = []           #Prime number (power) list
    sum_lst = []            #Sum of the divisors
    sums_divslst = []
    numbers_lst = []
    dd = trinum
    numbers_lst.append(dd)  #keep list of numders for comparison later
    odd_abundant =[]
    even_abundant = []
    abundant = []
    paired_abundant = set()
    filtered = []

#------------------Calculate divisors-----------------------
    while dd > 3:

        if not trinum % prim == 0: # Is there a modulus, if so, increase the Prime Number
            if count > 0: #Divisor counter
                kounter = count + 1
                power_lst.append(kounter)
            count = 0
            z += 1
            prim = prims[z]
            continue

        trinum = trinum / prim
        if not prim in div_lst:
            div_lst.append(prim)
        count += 1
        if trinum == 1:  #Divide down to 1, test the amount of divisors and
            kounter = count + 1   # if too low, increase the Triangle Number
            power_lst.append(kounter)


#----------Sum of divisors formula-----------------
            a = len(div_lst)
            b = a - 1   #starts at 0
            ans = 1
            #print("divlist,powerlist = ",div_lst,power_lst)
            '''Sum formula'''
            for i in range(b, -1, -1):
                c = ((div_lst[i] ** power_lst[i]) - 1) /(div_lst[i] - 1)
                sum_lst.append(c)

            '''Product of the sum list'''

            product = 1
            for i in sum_lst:
                product  *= i
            product = product - dd



#-----------gathering list of abundant numbers---------------------

            if product > dd :
                abundant.append(dd)

#-----------------------------------------------------------------



            count = 0
            z = 0
            prim = prims[z]
            increm +=1
            trinum = next(v)
            dd = trinum
            numbers_lst.append(dd)

            sum_lst = []
            div_lst = []
            power_lst = []

            continue

            if trinum == 2:
                break


 #---------End of While loop-------------------------

    #import pdb; pdb.set_trace()
#----------Gather paired abundants------------------

    sums =set() #Using a set for filtering later
    for item1 in abundant:
        for item2 in abundant:
            if item1+item2<28124:
                sums.add(item1+item2)

#------filter non-paired_abundant integers----------
    filtered = 0
    for j in range(1,28124):
        if j not in sums:
            filtered +=j
    print (filtered)


#------------------------------------------------------------------------

if __name__ == '__main__':
    main()
    print(time.time() - tt)