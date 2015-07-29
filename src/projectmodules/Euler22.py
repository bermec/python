#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rog
#
# Created:     09/10/2010
# Copyright:   (c) rog 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import re

def main():
    pass


f = open("names.txt",'r')

names = []

names = sorted(f.read().replace('"','').split(','),key=str)

i = 0
sum = 0
ans = 0

for string in names:
    i += 1
    chars = list(string)

    for x in chars:

        if x == 'A':
            t = 1
        elif x == 'B':
            t = 2
        elif x == 'C':
            t = 3
        elif x == 'D':
            t = 4
        elif x == 'E':
            t = 5
        elif x == 'F':
            t = 6
        elif x == 'G':
            t = 7
        elif x == 'H':
            t = 8
        elif x == 'I':
            t = 9
        elif x == 'J':
            t = 10
        elif x == 'K':
            t = 11
        elif x == 'L':
            t = 12
        elif x == 'M':
            t = 13
        elif x == 'N':
            t = 14
        elif x == 'O':
            t = 15
        elif x == 'P':
            t = 16
        elif x == 'Q':
            t = 17
        elif x == 'R':
            t = 18
        elif x == 'S':
            t = 19
        elif x == 'T':
            t = 20
        elif x == 'U':
            t = 21
        elif x == 'V':
            t = 22
        elif x == 'W':
            t = 23
        elif x == 'X':
            t = 24
        elif x == 'Y':
            t = 25
        else:
            t = 26
        sum += t
        ans += sum * i

        sum = 0

print(ans)
if __name__ == '__main__':
    main()