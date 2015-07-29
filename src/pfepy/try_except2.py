
astr = "Hello Bob"  #  a string
try:
    istr = int(astr)  #  got to be joking!
except:
    istr = -1

print("First", istr)


a = 123
print(type(a))
try:

       #  will do! bypasses the except
                      #  and carries on.
except:
    a = -1

print("Second ", a)
