str1 = 'qwertY key_board:  0.7763'
att = str1.find(':')
print att
num_str = str1[att + 1:]
print  num_str
num = float(num_str)
print num
print type(num)