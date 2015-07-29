#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rog
#
# Created:     27/09/2010
# Copyright:   (c) rog 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

'''Let d(n) be defined as the sum of proper divisors of n (numbers less than
 n which divide evenly into n).
If d(a) = b and d(b) = a, where a not equalÃ‚Â  b, then a and b are an amicable
pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.'''
import time
tt = time.time()
def main():
    pass

'''Empty list'''
g = []

def divsum(n):
    return sum(i for i in range(1, n) if not n % i)


'''work out the divisors from 10000 to 2'''
for x in range(10000, 2, -1):
    ''' check if amicable pair'''
    c = divsum(x)
    v = divsum(c)

    if v == x and v != c:
        g.append(divsum(x))
    else:
        continue

#print(len(g))
print(sum(g))



if __name__ == '__main__':
    main()
    print(time.time() - tt)