import sys

N = int(raw_input())

if(N<1 or N>10**6):
	sys.exit(0)

L = []
S = []

for i in xrange(N):
	word = raw_input()
	word = word.replace(" ", "")
	if(len(word)<2 or len(word)>10):
		sys.exit(0)
	L.append(word)

L.sort()

Q = int(raw_input())

if(Q<1 or Q>10**6):
	sys.exit(0)

for i in xrange(Q):
	word = raw_input()
	word = word.replace(" ", "")
	if(len(word)<2 or len(word)>10):
		sys.exit(0)
	S.append(word)

for word in S:
	if word in L:
		print L.index(word)+1
	else:
		print -1