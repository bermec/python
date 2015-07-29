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



a = 42
b = 37
def foo():
    global a
    a = 23
    b = 60
foo()
'''a is now 23, b is still 37'''


#Continue skips any other stages in the loop and continues with
# another iteration of the loop

if __name__ == '__main__':
    main()

