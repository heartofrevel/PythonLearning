testCases = int(raw_input())


for i in xrange(testCases):
	flag=True
	rowsAndColumns = raw_input()
	inputRowsAndColumns = rowsAndColumns.split()
	rows = int(inputRowsAndColumns[0])
	columns = int(inputRowsAndColumns[1])
	finalRows=list()

	for counter in xrange(rows):	
		row=raw_input()
		rowSplitted = list(row)
		finalRows.append(rowSplitted)
		print finalRows
	
	for i in xrange(len(finalRows[0])-1):
		tempRows = finalRows
		for j in xrange(len(finalRows)):
			del tempRows[j][i]
		print tempRows