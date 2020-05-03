exec("""
import re
import urllib.request
from bs4 import BeautifulSoup
prev=0
stock=input("Enter a stock symbol: ")
#for i in range (0, 100):
while 1:
	html = urllib.request.urlopen('https://www.marketwatch.com/investing/stock/'+stock)
	soup = BeautifulSoup(html, "lxml")
	data = soup.findAll(text=True)
	 
	def visible(element):
 	   if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
 	       return False
 	   elif re.match('<!--.*-->', str(element.encode('utf-8'))):
 	       return False
 	   return True

	result = filter(visible, data)


	mystring=(list(result))
	#print(len(mystring))
	length=len(mystring)
	spot=0
	for x in range (0, length):
		if mystring[x]=='Real time quote':
			#print(x)
			spot=x
	if mystring[spot+7]!=prev:
		print(mystring[spot+7])
	prev=mystring[spot+7]
""")

