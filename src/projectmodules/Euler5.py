import math
import time
import sys
sys.path.append("../")
from rogutil import *

def main():
    s = time.time()
    print("rogs program")



    secondloop = list(range(1, 21)) #
    passcount = 0
    mult = 0
    prime = [3,5,7,11,13,17,19]
    primeprocessed = multiplylist(prime)


    while 1:
        mult += 1
        total = primeprocessed * mult
        passcount = 0
        for j in secondloop:
            test = float(total) / float(j)

            if not isdecimal(test):
                passcount += 1

        if passcount == len(secondloop):
            print("if passcount == len(secondloop):", passcount, total, j, len(secondloop))
            print('TIME : ',time.time() - s,' seconds')
            exit()

if __name__ == '__main__':
    main()

