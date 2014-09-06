a=int(raw_input())

for i in xrange(a):
	x=raw_input()
	params = x.split()
	a = int(params[0])
	b = int(params[1])
	count = 0
	for j in xrange(a,b+1):
		if(j == int(str(j)[::-1])):
			count = count + 1
	print count 
