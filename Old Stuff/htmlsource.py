exec("""
import requests
from bs4 import BeautifulSoup
f = open('html.txt','w')
#target_class = "gb4"
#target_text = "Web History"
r = requests.get("https://www.marketwatch.com/investing/stock/amzn")
soup = BeautifulSoup(r.text, "lxml")
mystring=str(soup)
backwardanswer=""
answer=""
length=len(mystring)
for x in range (0, length):
	if mystring[x]=="c" and mystring[x+1]=="e" and mystring[x+3]=="/" and mystring[x+4]==">":
		#print(x)
		#print(mystring[x-17]+mystring[x-16]+mystring[x-15]+mystring[x-14]+mystring[x-13]+mystring[x-12])
		i=12
		while mystring[x-i]!='"':
			backwardanswer=backwardanswer+mystring[x-i]
			i=i+1
z=len(backwardanswer)-1
while z>=0:
	answer=answer+backwardanswer[z]
	z=z-1
print(answer)
f.write(mystring)
f.close()

""")
