fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	strippedLine= line.rstrip()
	words = strippedLine.split()
	for word in words:
		if word not in lst:
			lst.append(word)
	

lst.sort()
print(lst)