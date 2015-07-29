#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      rog
#
# Created:     02/08/2010
# Copyright:   (c) rog 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys
sys.path.append("../")
from rogutil import *
from random import randint
#import pdb; pdb.set_trace()
def main():
    pass
    secret = randint(1, 10)
    print("Welcome!")
    guess = 0
    while guess != secret:
        g = input("Guess the number!")
        guess = int(g)
        if guess == secret:
            print("You win!!")
        else:
            if guess > secret:
                print("Too high!")
            else:
                print("Too low!")
    print("Game over!")
                

   

if __name__ == '__main__':
    main()
