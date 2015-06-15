def get_row(string):
	list1 = string.split()
	list2 = []
	for item in list1:
		list2.append('Card('+"'"+item[0]+"','"+item[1]+"')")
	row1 = list2[0:5]
	row2 = list2[5:10]
	row3 = list2[10:13]
	row4 = list2[13:17]
	print 'row1 = ',row1
	print 'row2 = ',row2
	print 'row3 = ',row3
	print 'row4 = ',row4

def main():
	string = '''3S	9C	8C	7S	5S
6C	10D	8D	10C	8S
	7C	5C	7H
	2C	10H	AC'''
	get_row(string)

if __name__ == '__main__':
	main()