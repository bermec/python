#import sys
#sys.path.append("../")
#from rogutil import *

#import pdb; pdb.set_trace()

a = 3

while a < 18:
    LenChain = 1 #Length of chain being tested
    NumOut = 0   # Number that developed the longest chain
    chain = a
    LongChain = 0 #Longest chain
    
    sett = set()
    sett.add(a)
    while a > 1:
        z = a
        LenChain += 1
        if chain % 2 == 0:
            chain = chain/2

        else:
            chain = chain*3 + 1

        if chain == 1: #Each time chain arrives at 1 check length
            if LenChain > LongChain:
                LongChain = LenChain
                NumOut = a
            a += 1    #Reset values for next calculation
            chain = a
            LenChain = 0
    #if a == 1:
    print(NumOut,LongChain)
    exit()
