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

    '''Handle multiple exception types'''

    try:
        num = float(input("\nEnter a number: "))
    except ValueError:
        print("That was not a number!")

    print()




if __name__ == '__main__':
    main()
