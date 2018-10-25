import re
source = open('Dracula.txt')			#Opens text file 'Dracula.txt' so words can be read and regex can be used
onlineBook = source.read()
#print matchingWords

def amess(onlineBook):
	if type(onlineBook) != str:						#Type error makes sure argument is a string
		raise TypeError("Not a string!")

	match = re.findall(r"\w*at\b", onlineBook)			#Reg. expression that should find words ending with at in source file
	aboveThree =  []											#Empty list to hold words ending in at that are larger than 3
	for word in match:
		if len(word) >  3:						#If the words end in at and they contain four or more letters
			aboveThree.append(word)				#then add them to the empty list aboveThree
	print(aboveThree)
