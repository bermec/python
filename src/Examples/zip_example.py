#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rog
#
# Created:     27/09/2010
# Copyright:   (c) rog 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

#-------Zip---------------
xx = [1, 1, 3, 7, 5,10, 5, 7, 3]
y = [5, 6, 7, 3, 1, 22, 4, 7, 6]
a = list(zip(xx, y))

# [(1, 5)(1, 6).....]

#-----------Unzip----------
x2, y2 = zip(*a)

print(x2)

#[1, 1, 3, ......]

if __name__ == '__main__':
    main()