#import sys
#sys.path.append("../")
#from rogutil import *

#import pdb; pdb.set_trace()

a = 3
z = 0
LenChain = 0

while a < 500000:
    #LenChain = 1 #Length of chain being tested
    #NumOut = 0   # Number that developed the longest chain
    chain = a
    #LongChain = 0 #Longest chain
    #z = 0
    
    #sett = set()
    #sett.add(a)
    while chain != 1:
        z = a
        LenChain += 1
        if chain % 2 == 0:
            chain = chain/2
            #if chain in sett:
                #break

        else:
            chain = chain * 3 + 1
            #if chain in sett:
                #break
    a += 2

        #if chain == 1: #Each time chain  equates to 1 check LenChain
            #if LenChain > LongChain:
               # LongChain = LenChain
                #NumOut = chain
            #a += 1    #Reset values for next calculation
            #chain = a
            #LenChain = 0

print(a,LenChain)
exit()
