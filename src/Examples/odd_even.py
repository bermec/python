i = 2

while i <= 10 :
	if i % 2 == 0 :
		print(str(i) + ' is an even number')
	else :
		print(str(i) + ' is an odd number')
	i =+ 1
	
	#or this one
	
	
	def test(i):
		if not i & 1:
			return False
		else:
			return True
	print(test(i))

	