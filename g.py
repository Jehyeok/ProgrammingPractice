def numOfE() :
	num = len("next people")
	
	for char in "next people" :
		if char != 'e' :
			num -= 1
	return num

print numOfE()
