def input_raw():
    score = raw_input("Enter score: 0.1 to 1.0: ")
    return score



def set_variable(n):
    # set variable if passed trap
    s = float(n)

    return s

def in_range(s):
     # check if in range
    if not (0 < s <= 1):
        print "Out of range, try again: "
        input_raw()
    else:
        return s

	
def calc_grade(s):
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
    return grade


if __name__ == '__main__':


    score = input_raw()

    while score == float(score):
        # ValueError trap, eg 'one'
        try:
            float(score)
        except:
            print "Wrong input, try numeric"
            break

    ans = set_variable(score)
    s = in_range(ans)
    ans2 = calc_grade(s)
    print ans2
