#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rog
#
# Created:     06/10/2010
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
    * A leap year occurs on any year evenly divisible by 4, but not on a
     century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
 (1 Jan 1901 to 31 Dec 2000)?'''

'''To find the ordinal position of the day within the week for any date
 between Jan 1, 1901 and Dec 31 2099

      1.  Find the year_ordinal using the table of days before the
      first of the month

      2.  Calculate week_ordinal(1/1) as follows

          a = (year - 1901) modulo 28
          b = floor (a/4)
          week_ordinal(1/1) = (2 + a + b) modulo 7 + 1

      3.  Day of the Week = ((year_ordinal - 1) + (week_ordinal(1/1) - 1))
       modulo 7 + 1'''

import math

def main():
    pass

lst1 = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334] #std
lst2 = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335] #leap

sunday = 0
y = 0

while y < 12:

    for x in range(2000,1900,-1):
        a = (x - 1901) % 28
        z = x
        if z % 4 == 0:
            year_ordinal = lst2[y]

        else:
            year_ordinal = lst1[y]

        b = math.floor(a / 4)
        week_ordinal = (2 + a + b) % 7 + 1
        day_of_the_week = ((year_ordinal-1) + (week_ordinal - 1)) % 7 + 1

        if day_of_the_week == 7:
            sunday += 1
        if x == 1901:   #increment to next month
            y += 1
            continue
print("Year =  ", x," Day ",day_of_the_week,"month = ", y,"Sundays = ", sunday)
exit()

if __name__ == '__main__':
    main()