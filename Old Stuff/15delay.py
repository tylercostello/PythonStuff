import re
import time
import requests
from bs4 import BeautifulSoup
import datetime
now = datetime.datetime.now()
minute=now.minute+2
maxhour=1
minhour=6.5
#theend=False
currentminute=now.minute
prevminute=0
hour=now.hour
decimalminute=now.minute
decimalminute=float(decimalminute)/float(60)
hour=hour+decimalminute
f = open('portfoliostockprice.txt','a')
g = open('portfoliostockpriceandtime.txt','a')
#stock=input("Enter a stock symbol: ")
def mystockchecker(name):
	r = requests.get("https://www.wsj.com/search/term.html?KEYWORDS="+name)
	soup = BeautifulSoup(r.text, "html.parser")
	mystring=str(soup)
	answer=""
	a = re.search(r'("last")', mystring)
	#print(a.start())
	counter=7
	while mystring[a.start()+counter]!="<":
		#print(mystring[a.start()+counter])
		answer=answer+mystring[a.start()+counter]
		counter=counter+1
	counter=0
	#print(mystring[a.start()+7])
	total=float(answer)
	return total
while hour>=6.5 and hour<=13 and datetime.datetime.today().weekday()<5:
#while 1:
	now = datetime.datetime.now()
	if hour<13:
		theend=False
	currentminute=now.minute
	hour=now.hour
	decimalminute=now.minute
	decimalminute=float(decimalminute)/float(60)
	hour=hour+decimalminute
	#print(hour)

	if currentminute==0 or currentminute==15 or currentminute==30 or currentminute==45:
		if currentminute!=prevminute:
			sum=0
			sum=sum+mystockchecker("baba")
			sum=sum+5*mystockchecker("schx")
			sum=sum+2*mystockchecker("schg")
			sum=sum+mystockchecker("ryt")
			stringhour=str(hour)
			print(str(now))
			print(sum)
			f.write("\n")
			g.write("\n")
			g.write(str(now))
			g.write(" ")
			g.write(str(sum))
			f.write(str(sum))
	if now.hour==13 and theend==False:
		theend=True
		f.write("\t")
		f.write(str(now.month)+"-"+str(now.day)+"-"+str(now.year))
	prevminute=currentminute
	sum=0
	answer=""
	time.sleep(1)
f.close()

