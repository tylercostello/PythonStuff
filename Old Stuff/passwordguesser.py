exec("""
password=input("Password: ")
guess=['0']
spot=0
answer=''.join(guess)
length=len(guess)-1
while answer != password:
	answer=''.join(guess)
	length=len(guess)-1
	while guess[spot]=='{':
		guess[spot]='0'
		if spot<length:	
			guess[spot+1]=chr(ord(guess[spot+1]) + 1)
			answer=''.join(guess)
			spot=spot+1
		elif spot>=length:
			guess.append('0')
			spot=spot+1
	spot=0
	guess[spot]=chr(ord(guess[spot]) + 1)
print("success")
print(answer)
""")
