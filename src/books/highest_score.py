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


scores = []
names = []
result_f = open("results.txt")

for line in result_f:
    (name, score) = line.split()
    scores.append(float(score))
    names.append(name)
result_f.close()
scores.sort()
names.sort()
scores.reverse()
names.reverse()

print("The top scores were: ")
print(names[0] + " with " + str(scores[0]))
print(names[1] + " with " + str(scores[1]))
print(names[2] + " with " + str(scores[2]))

   

if __name__ == '__main__':
    main()
