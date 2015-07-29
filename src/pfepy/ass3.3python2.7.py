while True:
    try:
        userInput = float(raw_input("Enter number between 0 and 1: "))
    except ValueError:
        print"Not an integer!"
        continue
    else:
        print"Yes a float!"
        if (0 <= float(userInput) <= 1):
            print 'yes, in range, good one!'
            break
        else:
            print 'but, out of range!'
            continue
	

if (0.9 <= s <= 1.0):
    grade = "A"
elif (0.8 <= s <= 0.9):
    grade = "B"
elif (0.7 <= s <= 0.8):
    grade = "C"
elif (0.6 <= s <= 0.7):
    grade = "D"
else:
    (0.0 <= s <= 0.6)
    grade = "F"




print grade
