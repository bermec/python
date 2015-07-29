try:
    inp = raw_input("Enter Scores: ")
    scores = float(inp)
except :
    print "Error, please type correct value"
    quit()

if scores >= 0.9 and scores <= 1.0:
    print 'A'
elif scores >= 0.8 and scores < 0.9:
    print 'B'
elif scores >= 0.7 and scores < 0.8:
    print 'C'
elif scores >= 0.6 and scores < 0.7:
    print 'D'
elif scores < 0.6 :
    print 'F'
else :
    scores < 0.0 or scores > 1.0
    print 'error, score out of range'