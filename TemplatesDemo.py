from string import Template

'''
	Demonstrate the use of Template Class, also created a Custom Template to override the
	default delimiter('$') with '#'.
	Templates are used as place holder for data from source and can be printed later 
	according to placeholder.
	Uses : 
	1. Can be used to rename files according to templates. Very useful
	2. Extremely useful for web pages, because webpage follows the same template with 
	   different data.
'''


class CustomTemplate(Template):
	delimiter = '#'


def Main():
	cart = []
	cart.append(dict(item="Coke", price=30, qty=4))
	cart.append(dict(item="Cake", price=300, qty=2))
	cart.append(dict(item="Fish", price=90, qty=3))
	# t = Template("$qty x $item = $price")  #Default Template
	t = CustomTemplate("#qty x #item = #price")  #Custom Template
	total = 0 
	print "Cart : "
	for data in cart:
		# print t.safe_substitute(data)   #Will neglect the key errors, not good practice
		print t.substitute(data)
		total += data['price']

	print "Total : "+str(total)

if __name__ == "__main__":
	Main()