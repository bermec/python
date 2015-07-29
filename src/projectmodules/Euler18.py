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

def main():
    pass

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


#print("mystr = ",mystr)
def doif(lst, a,b,c,):
    mylist = list(lst)
    if mylist [5] [b] > mylist [5] [c]:
        mylist[4][a] = mylist[4][a] + mylist[5][b]
        print(" a = ",a)
    else:
        mylist[4][a] = mylist[4][a] + mylist[5][c]
    return mylist

def main():
    pass
    """ changes the above string into a list"""
    mylist = []
    for item in mystr.split("\n"):
        mylist.append(list(map(int,item.split(" "))))

    pprint(mylist)
    #print (" mylist 3 = ",mylist[3][1])



    #import pdb; pdb.set_trace()




    e = len(mylist[4])
    print("e = ",e)

    a, b, c, d = 0, 0, 1, 0
    while d in range(0,e,1):
        mylist = doif(mylist,a,b,c)
        print("a ",a)
        a +=1
        b += 1
        c += 1
        d += 1

    a, b, c, d = 0, 0, 1, 0
    while d in range(0,e - 1,1):
        mylist = doif(mylist,a,b,c)
        print("a ",a)
        a +=1
        b += 1
        c += 1
        d += 1

    print("mylist [4] =  ",mylist[4])
    #mylist[4][1] = mylist[4][1] + 4
    print("mylist [4] =  ",mylist[4])
    exit()






'''
    a, b, c = 1, 3, 4
    while a in range(1,3,1):
        mylist = doif(mylist,a,b,c)
        print("a ",a)
        a +=1
        b += 1
        c += 1
    print(mylist)

    a, b, c = 0, 1, 2
    while a in range(0,1,1):
        mylist = doif(mylist,a,b,c)
        print("a ",a)
        a +=1
        b += 1
        c += 1

    print ("Total = ",mylist[0])
    exit()'''



if __name__ == '__main__':
    main()

if __name__ == '__main__':
    main()
