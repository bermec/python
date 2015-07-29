
astr = "Hello Bob"  #  a string
try:
    istr = int(astr)  #  got to be joking!
except:
    istr = -1

print("First", istr)


astr = "123"
try:
    istr = int(astr) #  will do! bypasses the except
                      #  and carries on.
except:
    istr = -1

print("Second ", istr)
