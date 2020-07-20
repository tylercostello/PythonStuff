exec("""
number=0
message=["k"]
length=len(message)-1
spot=0
loops=input("How many replies?")
counter=0
f = open('loops.txt','w')
str1 = ''.join(message)
 

while number != loops:
	length=len(message)-1
	if spot!=length:
		if message[spot]=="k":
			message[spot]="o"
			spot=spot+1
			message.insert(spot, "k")
			spot=spot+1
			#print(message)
		elif message[spot]=="o":
			message[spot]="k"
			spot=spot+1
			message.insert(spot, "o")
			spot=spot+1
			#print(message)
	elif spot==length:
		#print(spot)
		#print(length)
		#print("spot: ",spot)
		if message[spot]=="k":
			message[spot]="o"
			spot=spot+1
			message.append("k")
			spot=spot+1
			#print(3)
			#print(message)
		elif message[spot]=="o":
			message[spot]="k"
			spot=spot+1
			message.append("o")
			spot=spot+1
			#print(4)
			#print(message)
	#print("End: ",message)
	if spot==length+2:
		number=number+1
		spot=0
		print(number)
		str1 = ''.join(message)
		f.write(str1)
		f.write(",")


	
f.write(str1)
f.close()
""")