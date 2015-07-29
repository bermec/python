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
import pdb; pdb.set_trace()

import urllib.request
page = urllib.request.urlopen("http://www.beans-r-us.biz/prices.html")
text = page.read().decode("utf8")

where = text.find(">$")

start_of_price = where + 2
end_of_price = start_of_price + 4

price = text[start_of_price:end_of_price]

print(price)
exit()
def main():
    pass

    print(text)

   

if __name__ == '__main__':
    main()
