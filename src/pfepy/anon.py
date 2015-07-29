prompt = input("Enter a score between 0 and 1.0 \n")
grade = float(prompt)
try:
    if (0.9 <= grade <= 1.0):
       print ("A")
    elif (0.8 <= grade <= 0.9):
        print ("B")
    elif (0.7 <= grade <= 0.8):
        print ("C")
    elif (0.6 <= grade <= 0.7):
        print ("D")
    else:
        print ("F")
except ValueError:
    print ("You didn't enter a correct score.")
