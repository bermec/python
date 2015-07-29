#!/usr/bin/env python
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

import sys
sys.path.append("../")
from rogutil import *
import time
import urllib.request
def get_price():
    page = urllib.request.urlopen("http://www.beans-r-us.biz/prices.html")
    text = page.read().decode("utf8")

    where = text.find(">$")

    start_of_price = where + 2
    end_of_price = start_of_price + 4
    
    return float(text[start_of_price:end_of_price])

def main():
    price = 99.99
    while price > 4.23:
        time.sleep(6)
        price = get_price()
        print(price)
    print("final price:", price)

if __name__ == '__main__':
    main()
