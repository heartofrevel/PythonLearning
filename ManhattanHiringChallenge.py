testCases=int(raw_input())

for i in xrange(testCases):
	word=raw_input()
	splitted=word.split()
	n=len(splitted)
	new = ""
	for j in reversed(splitted):
		new = new+j+" "
	print new