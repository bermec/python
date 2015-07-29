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

nums = [1, 2, 3 ,4, 5, ]
squares = []
for n in nums():
    squares.append(n * n)

'''Used often, now turned into an operator called 'List Comprehension'
Here is an example'''

nums = [1, 2, 3 ,4, 5, ]
squares = [x * x for n in nums]


if __name__ == '__main__':
    main()

