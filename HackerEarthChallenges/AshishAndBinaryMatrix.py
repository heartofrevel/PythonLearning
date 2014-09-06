import copy
import sys

testCases = int(raw_input())

if(testCases < 1 or testCases > 100):
	sys.exit(0)

for i in xrange(testCases):
	flag=False
	rowsAndColumns = raw_input()
	inputRowsAndColumns = rowsAndColumns.split()
	rows = int(inputRowsAndColumns[0])
	columns = int(inputRowsAndColumns[1])

	if(rows < 1 or rows > 1000 or columns < 2 or columns > 1000 ):
		sys.exit(0)

	finalRows=list()

	for counter in xrange(rows):	
		row=raw_input()
		rowSplitted = list(row)
		finalRows.append(rowSplitted)
		
	
	for i in xrange(len(finalRows[0])-1):
		tempRows = copy.deepcopy(finalRows)
		for j in xrange(len(finalRows)):
			del tempRows[j][i]

		count = 0
		for n in xrange(len(tempRows)-1):
			if tempRows[n] != tempRows[n+1]:
				flag = True
			else:
				flag = False
				break
				
		if(flag == True):
			break

	if flag == True:
		print "Yes"
	else:
		print "No"
