#import sys
#sys.path.append("../")
#from rogutil import *

#import pdb; pdb.set_trace()

a = 3
z = 3
LenChain = 0
sett = set()

while a < 5000:
    #LenChain = 1 #Length of chain being tested
    #NumOut = 0   # Number that developed the longest chain
    a = max(sett)
    sett = set()
    chain = a
    #LongChain = 0 #Longest chain
    #z = 0


    sett.add(a)
    while chain != 1:
        z = a
        LenChain += 1
        if chain % 2 == 0:
            chain = chain
            z = max(sett)
            #if chain in sett:
                #break

        else:
            chain = chain * 3 + 1
            z = max(sett)
            #if chain in sett:
                #break
    a = z
    z = 0

        #if chain == 1: #Each time chain  equates to 1 check LenChain
            #if LenChain > LongChain:
               # LongChain = LenChain
                #NumOut = chain
            #a += 1    #Reset values for next calculation
            #chain = a
            #LenChain = 0

print(a,LenChain)
exit()
