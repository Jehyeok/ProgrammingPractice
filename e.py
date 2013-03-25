def Test(num) :
	if num > 0 and num < 10 :
		return num + 10
	elif num >= 10 and num < 100 :
		return num * 0.1
	else :
		return False

x = raw_input("input message : ")
print Test(int(x))
