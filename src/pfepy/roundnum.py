def round_sum(a, b, c):
    a = round10(a)
    b = round10(b)
    c = round10(c)
    return a + b + c


def round10(num):
    num2 = str(num)
    num3 = int(num2)
    end_num = int(num2[-1])
    if (6 <= end_num <= 9):
        num = num + (10 - end_num)
        return num
    else:
        num = num - end_num
        return num


ans = round10(102)
print ans