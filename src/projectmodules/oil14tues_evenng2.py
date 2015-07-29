
import time
x = 3
chain_count = 0
sett = set()
lst = []
chain = 0
tt = time.time()

def increment_x(n):
    ''' increments x and checks
     it is not in the set '''
    for x in range(n,1000000):
        global sett
        if x not in sett:
            return x

chain = increment_x(x)
x = chain
while chain != 1:
    if chain % 2 == 0:
        chain //= 2
    else:
        chain = (3 * chain) + 1
    sett.add(chain)
    chain_count += 1
    lst.append(chain_count)




print(max(lst))
print(time.time() - tt)
