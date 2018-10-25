import re
source = open('Dracula.txt')			#Opens text file 'Dracula.txt' so words can be read and regex can be used
onlineBook = source.read()
#print matchingWords

def amess(onlineBook):
	if type(onlineBook) != str:						#Type error makes sure argument is a string
		raise TypeError("Not a string!")

	match = re.findall(r"\w*at\b", onlineBook)			#Reg. expression that should find words ending with at in source file
	aboveThree =  []											#Empty list to hold words ending in at
	for word in match:
		if len(word) >  3:
			aboveThree.append(word)
	print(aboveThree)
