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

def main():
    pass


scores = {}

result_f = open("results.txt")

for line in result_f:
    (name, score) = line.split()
    scores[score] = name
   
result_f.close()


print("The top scores were: ")

for each_score in sorted(scores.keys(), reverse = True):
    print("Surfer " + scores[each_score] + " scored " + each_score)
   

if __name__ == '__main__':
    main()






