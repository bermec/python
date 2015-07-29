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


def main():
    pass


    while True:
        s = (input("Enter something :"))
        if s == "quit":
            break
        print("Length of the string is ", len(s))
    print("done")

if __name__ == '__main__':
    main()

#The loop will not be broken until 'quit' is entered
# Can be used with the FOR loop also