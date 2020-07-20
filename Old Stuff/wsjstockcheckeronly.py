import re
import requests
import time
from bs4 import BeautifulSoup
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
print(mystockchecker("MSFT"))