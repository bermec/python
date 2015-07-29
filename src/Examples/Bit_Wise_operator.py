
'''&	Binary AND Operator copies a bit to the 
result if it exists in both operands. 	(a & b) will 
give 12 which is 0000 1100'''
n = 3

def test(n):
    if not n & 1:
        return False
    else:
        return True 
print(test(n))