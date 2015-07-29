
import time
#import cProfile

tt = time.time()
LongChain = 0 # Longest chain
def main():
        sett = set()
        LenChain = 1 # Length of chain being tested
        NumOut = 0   # Number that developed the longest chain

        numbr = 3    # number to be tested
        chain = numbr
        while numbr < 1000000:
                if numbr in sett:
                        numbr += 1
                        chain = numbr
                        continue
                LenChain += 1

        #-----------------------------------------

                if chain % 2 == 0:
                        chain = chain/2

                else:
                        chain = chain*3 + 1
        #-----------------------------------------
                ''' Keeping the numbers in the set from up to 999999
                only cut 12secs from the program'''
                if chain <= 1000000:
                        sett.add(chain)
        #-----------------------------------------
                if chain == 1: #Each time chain arrives at 1 check length
                        if LenChain > LongChain:
                                LongChain = LenChain
                                NumOut = numbr
                        numbr += 1    #Reset values for next calculation
                        chain = numbr
                        LenChain = 0
print(LongChain)
print(time.time() - tt," secs.")
exit()

#cProfile.run('main()')
main