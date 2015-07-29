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
from pprint import pprint

def doif(lst, a,b,c,str_upper,str_lower):
    mylist = list(lst)
    if mylist [str_lower] [b] > mylist [str_lower] [c]:
        mylist[str_upper][a] = mylist[str_upper][a] + mylist[str_lower][b]
    else:
        mylist[str_upper][a] = mylist[str_upper][a] + mylist[str_lower][c]
    return mylist



mystr = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''



def main():
    pass

    """ changes the above string into a list"""
    mylist = []
    for item in mystr.split("\n"):
        mylist.append(list(map(int,item.split(" "))))

    pprint(mylist)

    #import pdb; pdb.set_trace()

    '''start at the bottom two rows'''
    str_upper, str_lower = len(mylist[-1])-2,len(mylist[-1])-1
    e = len(mylist[str_upper])

    a, b, c, d = 0, 0, 1, 0
    while e != 0:
        while d in range(0,e,1):
            mylist = doif(mylist,a,b,c, str_upper, str_lower)
            a += 1
            b += 1
            c += 1
            d += 1
        d, a, b, c = 0, 0, 0, 1
        str_upper -=1
        str_lower -=1
        e -= 1

    print(mylist[0])

    exit()

if __name__ == '__main__':
    main()



