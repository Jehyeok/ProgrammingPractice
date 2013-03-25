import math
	
x1 = input('x1')
y1 = input('y1')
x2 = input('x2')
y2 = input('y2')

def length(x1, y1, x2, y2) :
	dotlen = math.sqrt((x2-x1)**2 + (y2-y1)**2)
	return dotlen

print length(x1, y1, x2, y2)
