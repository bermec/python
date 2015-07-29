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
#import pdb; pdb.set_trace()

def main():
    pass

    a = 100
    
    fact_sum = []
    
    while a > 0:
        tri_num = (a * (a + 1)) / 2
        fact_sum.append(tri_num)
        a -= 1
        
        
    print(sum(fact_sum))
    exit()

   



if __name__ == '__main__':
    #pdb.runcall(main)
    main()