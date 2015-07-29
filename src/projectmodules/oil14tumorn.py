
import time
x = 3
chain_count = 0
sett = set()
val_dict ={}
chain = 1
temp = 0
tt = time.time()

def increment_x(n):
    for x in range(n,1000000):
        global sett
        if x not in sett:
            return x

while x < 8:


    chain = increment_x(x)
    x = chain
    temp = chain

    while chain != 1:

        if chain % 2 == 0:
             chain //= 2
        else:
            chain = chain * 3 + 1
        sett.add(chain)
        chain_count += 1
        if chain == 1:
            x += 1
            val_dict = {temp: chain_count}
            chain_count = 0
            break
print('val_dict: ',val_dict)
valueslst =  val_dict.values()
large = max(valueslst)
keys = [x for x, y in val_dict.items() if y == large]
print(keys, " key")
print(max(valueslst))
print(time.time() - tt)