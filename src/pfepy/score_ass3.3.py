

score = raw_input("Enter score :")


score = float(score)
s = score

if s < 1.0 and s >= 0.9 :
	grade = "A"
elif s < 0.9 and s >= 0.8:
	grade = "B"
elif s < 0.8 and s >= 0.7:
	grade = "C"
elif s < 0.7 and s >= 0.6:
	grade = "D"
elif s < 0.6 and s >= 0.0:
	grade = "F"
else:
    print('Out of range, try again')
    quit()

	
print grade

