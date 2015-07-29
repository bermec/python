#---------
# Name:        module1
# Purpose:
#
# Author:      rog
#
# Created:     04/08/2010
# Copyright:   (c) rog 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

'''Let d(n) be defined as the sum of proper divisors of n (numbers less than
 n which divide evenly into n).
If d(a) = b and d(b) = a, where a, b, then a and b are an amicable pair and
 each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.'''


import sys
sys.path.append("../")
from rogutil import *
import time
tt = time.time()


def main():
    # ------------------
    # PROGRAM CONFIG


    # INIT VARIABLES
    result = 0
    count = 0
    increm = 1

    '''generator for trinum'''
    v = (x for x in range(10000, 2, -1))
    trinum = next(v)

    kounter = 0     # errr... counter
    prim = 0        # The Prime Number for division of the Triangle number
    i, z = 0, 0
    prims = gen_x(2000, gen_primes)     # prime number genny
    prim = prims[z]                     # For incrementing the Prime Number
    div_lst = []            #Divisor list
    power_lst = []           #Prime number (power) list
    sum_lst = []            #Sum of the divisors
    sums_divslst = []
    numbers_lst = []
    dd = trinum
    numbers_lst.append(dd)  #keep list of numders for comparison later

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
            b = a - 1

            ans = 1
            '''Sum formula'''
            for i in range(b, -1, -1):
                c = ((div_lst[i] ** power_lst[i] - 1) /(div_lst[i] - 1))
                sum_lst.append(int(c))


            '''Product of the sum list'''

            product = 1
            for i in sum_lst:
                product *= i


            sums_divslst.append(product -dd)

#----------End of divisors formula---divsum_lst-------------

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
    sums_divslst.append(1)       # Evens up the lists


    a = list(zip(numbers_lst, sums_divslst))

    b = []
    def checktuple(tpl, mylist):
        result = False
        if tpl[::-1] in mylist:
            #print("found", tpl[::-1])
            result = True
        return result

    def checkpair(tpl, mylist): #Identical pairs are not amicable
        result = False
        a = tpl[0]
        b = tpl[1]
        if a / b == 1:
            #print("Pair")
            result = True
        return result

    for item in a:
        if checkpair(item, a):
            continue
        if checktuple(item, a):
            if not item[::-1] in b:
                b.append(item)


    '''flatten the list b'''

    h = [j for i in b for j in i]

    #print(h)
    print("answer = ",sum(h))


if __name__ == '__main__':
    main()
    print(time.time() - tt)