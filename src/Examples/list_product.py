#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rog
#
# Created:     24/09/2010
# Copyright:   (c) rog 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import operator

def main():
    pass

lst= [ 7, 4, 7]
lst2 = []


product = 1
for i in lst:
    product *= i

lst2.append(product)

print(lst2)

if __name__ == '__main__':
    main()