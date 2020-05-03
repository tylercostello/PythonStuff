exec("""
number=4
value=3
m=1000000007
while number!=1000:
	value=2*value-1
	number=number+1
	if number!=1000:
		value=2*value+1
		number=number+1
print(number)
print(value)
print(value%m)
#print(number)
#print(value)
#print(value%m)
""")



