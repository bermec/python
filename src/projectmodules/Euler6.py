'''
Created on 26 Jul 2010

@author: rog
'''
import time
t = time.time()

def main():
    '''find the difference between the sum of the square
    of the first 100 natural numbers and the square of he sum.'''

    n = float(100)
    ans1 = 0.0
    ans = 0.0
    ans3 = 0.0
    a = 1.0
    d = 1.0


    ans1 = (n ** 3 / 3) + (n ** 2 / 2) + ( n / 6 )

    ans =  ((n / 2) *  ( (2 * a) + ( n - 1) * d)) ** 2
    ans3 = ans - ans1

    print(ans3)
    print(time.time() -t)
if __name__ == '__main__':
    main()

