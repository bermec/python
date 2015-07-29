
# Author:      rog
#
# Created:     04/08/2010
# Copyright:   (c) rog 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys
sys.path.append("../")
from rogutil import *

import time
tt = time.time()
def main():
    a = 600851475143
    x = 2
    while a < a+1:
        if a == x:
            print(a)
            return
        if a%x == 0:
            a = a/x
            continue
        else:
            x += 1
            if x % 2 ==0:
               x += 1


    '''# Start program
    def fib():
        a = 0
        b = 1
        while 1:
            yield a

            b = a + b
            #a = b
            a, b = b, a + b

    i = 0
    for num in fib():
        i += 1
        print(num)
        if i == 10:
            break
    # End program
    time.sleep(2)'''
if __name__ == '__main__':

    main()
    print(time.time() - tt)
