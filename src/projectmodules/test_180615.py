LenChain = 1 #Length of chain being tested

sett = set()


a = 217
while a != 1:

    LenChain += 1
    if a % 2 == 0:
        a = a/2

    else:
        a = a*3 + 1
    sett .add(a)

    if a == 1:
        print(max(sett))#Each time chain arrives at 1 check length
