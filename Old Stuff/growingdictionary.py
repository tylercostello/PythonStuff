exec("""
words=["apple"]
definitions=["red fruit"]

while 1:
	found=False
	length=len(words)
	currentword=input("Enter a word: ")
	for x in range (0,length):
		if currentword==words[x]:
			print(definitions[x])
			x=length
			found=True
	if found==False:
		words.append(currentword)
		currentdefinition=input("Enter the definition: ")
		definitions.append(currentdefinition)
		print(words)
		print(definitions)
""")

