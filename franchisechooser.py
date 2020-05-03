exec("""
amount=0
years=3
investment=297025
print("years",1)
print("amount",-250000)
print("invesment",250000)
print("investment is better")
print("years",2)
print("amount",-250000)
print("invesment",272500)
print("investment is better")
print("years",years)
print("amount",-175000)
print("invesment",investment)
print("investment is better")
while years<100:
	years=years+1
	amount=amount+120000*(1.07**(years-4))
	investment=250000*(1.09**(years-1))
	print("years",years)
	print("amount",amount-250000)
	print("invesment",investment)
	if (amount-250000)>=investment:
		print("franchise is better")
	else:
		print("investment is better")
	print("")
""")
