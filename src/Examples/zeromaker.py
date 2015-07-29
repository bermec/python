def zeromaker(curnum, length):
    numofzero = length - len(str(curnum))
    string = "0" * numofzero
    return string + str(curnum)
