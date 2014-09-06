import optparse
import re

def Main():
	parser = optparse.OptionParser("Usage %prog : -w <word> -f <file>")
	parser.add_option("-w", "--word", dest="word", type="string", help="Specify a word to search for")
	parser.add_option("-f", "--file", dest="fileName", type="string", help="Specify a file to search in")
	parser.add_option("-m", "--match", action="store_true", dest="matchWord", default=False, help="Match Exact Word")
	parser.add_option("-c", "--case-sensitive", action="store_true", dest="caseSensitive", default=False, help="Case Sensitive Search")
	(options, args) = parser.parse_args()
	if (options.word== None or options.fileName==None):
		print parser.print_help()
		exit(0)
	else:
		word = options.word
		fileName = options.fileName

	searchFile = open(fileName)
	lineNum = 0 

	for line in searchFile.readlines():
		line = line.strip('\n\r')
		lineNum += 1
		if(options.caseSensitive and options.matchWord):
			searchResult = re.match(word, line, re.M)
		elif(options.caseSensitive and not(options.matchWord)):
			searchResult = re.search(word, line, re.M)
		elif(not(options.caseSensitive) and options.matchWord):
			searchResult = re.match(word, line, re.M|re.I)
		else:
			searchResult = re.search(word, line, re.M|re.I)

		if searchResult:
			print str(lineNum)+": "+line

if __name__ == "__main__":
	Main()
