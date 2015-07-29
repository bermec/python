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

def main():
    pass
'''propogate a list'''
lst = [i for i in range(9,1,-1)]
print(lst)
'''[9, 8, 7, ....]'''

'''similar, but use a generator'''
g = (x for x in range(9,1,-1))
print(next(g))
'''9'''
print(next(g))
'''8'''
trinum = next(g)
print(trinum)
'''7'''


if __name__ == '__main__':
    main()