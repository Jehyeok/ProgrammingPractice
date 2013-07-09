def printOneDan(dan):
	for i in range(1, 10):
		print "%3d" % (i * dan),

def gooGooDan():
	for dan in range(1, 10):
		printOneDan(dan)
		print

gooGooDan()