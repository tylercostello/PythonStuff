exec("""
import requests
from bs4 import BeautifulSoup
f = open('stockprice.txt','w')
stock=input("Enter a stock symbol: ")
r = requests.get("https://www.marketwatch.com/investing/stock/"+stock)
soup = BeautifulSoup(r.text, "lxml")
mystring=str(soup)
print(soup)
backwardanswer=""
answer=""
length=len(mystring)
for x in range (0, length):
	if mystring[x]=="c" and mystring[x+1]=="e" and mystring[x+3]=="/" and mystring[x+4]==">":
		i=12
		while mystring[x-i]!='"':
			backwardanswer=backwardanswer+mystring[x-i]
			i=i+1
z=len(backwardanswer)-1
while z>=0:
	answer=answer+backwardanswer[z]
	z=z-1
f.write(answer)
print(answer)
f.close()
""")
