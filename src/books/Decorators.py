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


def main():
    pass

def square(x):
    return x * x
square = trace(square)

'''the shorthand for this is:'''

@trace
def square(x):
    return x * x

'''Good example'''
#-----------------------------------------------------
def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world"

print hello() ''' returns <b><i>hello world</i></b>'''

#-------------------------------------------------------

if __name__ == '__main__':
    main()

