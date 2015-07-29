largest = None
smallest = None
while True:
    inp = raw_input("enter a number: ")
    if inp == "done" : break
    if len(inp) < 1 : break
    try :
        num = int(inp)
    except:
        print "invalid input"
        continue
    for itevar in [4,5,7] :
        if  largest is None or largest < num :
            largest = num
    print "Maximum: ",  largest
    for itevar in [4,5,7] :
        if smallest is None or smallest > num :
                smallest = num
    print "Minimum: ", smallest


