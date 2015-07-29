#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rog
#
# Created:     30/09/2010
# Copyright:   (c) rog 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
'''You are given the following information, but you may prefer to do some
 research for yourself.

    * 1 Jan 1900 was a Monday.
    * Thirty days has September,
      April, June and November.
      All the rest have thirty-one,
      Saving February alone,
      Which has twenty-eight, rain or shine.
      And on leap years, twenty-nine.
    * A leap year occurs on any year evenly divisible by 4, but not on
    a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
 century (1 Jan 1901 to 31 Dec 2000)?'''


def main():
    pass

''' Find the year_ordinal using the table of days before the first of the month'''

      2.  Calculate week_ordinal(1/1) as follows

          a = (year - 1901) modulo 28
          b = floor (a/4)
          week_ordinal(1/1) = (2 + a + b) modulo 7 + 1

      3.  Day of the Week = ((year_ordinal - 1) + (week_ordinal(1/1) - 1)) modulo 7 + 1

if __name__ == '__main__':
    main()