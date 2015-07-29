# Hey guys i'm having an issue.  this is my code:


score = input ("Please enter a score between 0.0 & 1.0:")
score = float(score)
if score >= 0.9:
    print ("A")
elif score >= 0.8:
    print ("B")
elif score >= 0.7:
  print ("C")
elif score >= 0.6:
  print ("D")
elif score < 0.6:
    print( "F")

try:
    score > float(1.0)
    score < float(0.0)
    score = s
except:
    score > float(1.0)
    print ("Please enter a value less than 1.0")
    score < float(0.0)
    print ("Please enter a value greater than 0.0")
