#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rog
#
# Created:     23/08/2010
# Copyright:   (c) rog 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    text_file = open("mmini.txt", "r")
    mytext = text_file.readlines()
    print(mytext)

    mylist = []
    for item in mytext:
        mylist.append(list(map(int,item.split(" "))))
    print(mylist)
    exit()

if __name__ == '__main__':
    main()