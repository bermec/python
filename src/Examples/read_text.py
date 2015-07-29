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
#import pdb; pdb.set_trace()

def main():
    pass
    '''Using readlines'''
    text_file = open("mini.txt", "r")
    mytext = text_file.readlines()
    print("Text using 'readlines :  '",mytext)

    '''then convert to a List'''

    mylist = []
    for item in mytext:
        mylist.append(list(map(int,item.split(" "))))
    print("Now convert to split list :  ",mylist)

    '''using read'''

    text_file = open("mini.txt", "r")
    mytext = text_file.read()
    print("Using 'read' : /n ", mytext)


    exit()



if __name__ == '__main__':
    main()
