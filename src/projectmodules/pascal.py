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


    def pascal(n):

        """Prints n first lines of Pascal`s triangle

        author: DR#m <dnpsite.narod.ru>
        last rev 20.03.05"""
        l=[1]
        p=[]
        for i in range(n):
            l2=[1]
            for j in range(len(l)-1):
                l2.append(l[j]+l[j+1])
            l2.append(1)
            print (l)
            l=l2

            outputt = squarelist(l)

            #a1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,]
            #a2 =[ x**2 for x in a1]
            print(outputt)

    pascal(20)
if __name__ == '__main__':
    main()
