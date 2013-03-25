def odd(string, length) :
	i = length-1;
	j = 0;

	while i/2+1 > 0 :
		if string[j] != string[i] :
			check = 0;
			break;
		else :
			check = 1;
		i -= 1;
		j += 1;

	return check;

x = raw_input("input message : ")
check = odd(x, len(x));

if check == 1 :
	print "correct";
else :
	print "incorrect";
