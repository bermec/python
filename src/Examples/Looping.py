#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rog
#
# Created:     15/10/2010
# Copyright:   (c) rog 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

a = [1,2,3]
b = [2,3,4]
c = []
for x in range(len(a)-1,-1,-1):
    for y in range(0,3,1):
        c =a[x] * b[y]
        print(c)





if __name__ == '__main__':
    main()