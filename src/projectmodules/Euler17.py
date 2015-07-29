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
"""
How many letters would be needed to write all the numbers in words
from 1 to 1000?
"""

import sys
sys.path.append("../")
from rogutil import *

dict_thou = {1:11,0:0}
dict_hund = {9:14,8:15,7:15,6:13,5:14,4:14,3:15,2:13,1:13,0:0}
dict_tens = {9:6,8:6,7:7,6:5,5:5,4:5,3:6,2:6,0:0}
dict_teens = {19:8,18:8,17:9,16:7,15:7,14:8,13:8,12:6,11:6,10:3}
dict_singl = {9:4,8:5,7:5,6:3,5:4,4:4,3:5,2:3,1:3,0:0}
dict_hundreds = {9:11,8:12,7:12,6:10,5:11,4:11,3:12,2:10,1:10,0:0}

def main():
        cnt = 0
        total = 0
        for number_for_test in range(1000,0,-1):

            number_for_test = zeromaker(str(number_for_test), 4)


            ''' Is this 100, 200 etc? '''
            if int(number_for_test [2]) == 0 and \
               int(number_for_test [3]) == 0 and \
               int(number_for_test [1]) > 0:
                hundreds = (number_for_test[1])
                hundred = int(hundreds)
                hh = dict_hundreds[hundred]
                y = hh
                total = total + y
                hh,hundreds,hundred,y = 0,0,0,0
                continue


            ''' is it between ten and 19? '''
            if int(number_for_test [2]) == 1:
                teens = (number_for_test[2])+(number_for_test[3])
                teen = int(teens)
                s = int(number_for_test [1])
                teenager = dict_teens[teen]
                v = dict_hund[s]
                y = v + teenager
                total = total + y
                r,s,v,y = 0,0,0,0
                continue

            '''If statement required to cut out 200, 300 etc'''
            if number_for_test [2] != 0 and \
               number_for_test [3] != 0:
                r = int(number_for_test [0])
                s = int(number_for_test [1])
                t = int(number_for_test [2])
                u = int(number_for_test [3])
                z = dict_thou[r]
                v = dict_hund[s]
                w = dict_tens[t]
                x = dict_singl[u]
                y = v + w + x + z
                total = total + y
                r,s,t,u,v,w,x,y,z = 0,0,0,0,0,0,0,0,0
                y = 0
                continue
        print("Total = ", total,"Count = ",cnt)

    #pass


if __name__ == '__main__':
    import time
    t = time.time()
    main()
    print(time.time() - t)
