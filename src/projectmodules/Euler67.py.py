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

def main():
    pass
    text_file = open("triangle.txt", "r")
    mytext = text_file.readlines()
    print(mytext)

    mylist = []
    for item in mytext:
        mylist.append(list(map(int,item.split(" "))))


    print(mylist)

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
