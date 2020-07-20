exec("""
def encrypt(x):
	length=len(x)
	x=list(x)
	z=list(x)
	for a in range(0,int(round(length/2,0)-1)):
		a=2*a
		x[a]=z[a+1]
		x[a+1]=z[a]
	for y in range(length):
		x[y]=chr(ord(x[y])+y+1)
	''.join(x)
	return(x)
def decrypt(x):
	length=len(x)
	for y in range(length):
		x[y]=chr(ord(x[y])-y-1)
	x=list(x)
	z=list(x)
	for a in range(0,int(round(length/2,0)-1)):
		a=2*a
		x[a]=z[a+1]
		x[a+1]=z[a]
	''.join(x)
	return(x)
thepass=input("Enter a password: ")
times=int(input("How many times do you want it encrypted? "))
for counter in range(0,times):
	thepass=encrypt(thepass)
print("Encrypted: ",thepass)
for counter in range(0,times):
	thepass=decrypt(thepass)
print("Decrypted: ",thepass)
""")