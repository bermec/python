x = raw_input("Enter your score between 0.0 and 1.0: ")


try:
    score = float(x)

    if score <= 1.0:
        if score >= 0.0:
            if score >= 0.9:
                print("A")
            elif score >= 0.8:
                print("B")
            elif score >= 0.7:
                print("C")
            elif score >= 0.6:    #This line
                print("D")
            elif score < 0.6:
                print("F")
            else:
                print("Out of range. Try again.")


except:
    print("Score is out of range or not a number. Please try again.")