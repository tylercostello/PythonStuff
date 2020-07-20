import re
import time
import requests
from bs4 import BeautifulSoup
from decimal import Decimal
import datetime
import smtplib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
now = datetime.datetime.now()
minute=now.minute+2
maxhour=1
emailstatus=False
minhour=6.5
dateprinted=False
currentminute=now.minute
prevminute=0
hour=now.hour
decimalminute=now.minute
decimalminute=float(decimalminute)/float(60)
hour=hour+decimalminute
e = open('prevday.txt','r')
prevday=e.read()
prevday=float(prevday)
#print(prevday)
e.close()

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
#print(hour)
while hour>=6.5 and hour<=13.1 and datetime.datetime.today().weekday()<5:
#while 1:
    now = datetime.datetime.now()
    currentminute=now.minute
    hour=now.hour
    decimalminute=now.minute
    decimalminute=float(decimalminute)/float(60)
    hour=hour+decimalminute
    #print(hour)
    #if 1:
    if currentminute==0 or currentminute==15 or currentminute==30 or currentminute==45:
        if currentminute!=prevminute:
            f = open('portfoliostockprice.txt','a')
            g = open('portfoliostockpriceandtime.txt','a')
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
    if now.hour==6 and now.minute==30 and dateprinted==False:
        f = open('portfoliostockprice.txt','a')
        emailstatus=False
        dateprinted=True
        f.write("\t")
        f.write(str(now.month)+"-"+str(now.day)+"-"+str(now.year))
    prevminute=currentminute

    answer=""
    time.sleep(1)
    #if now.hour==17:
    if now.hour==13:
            f.close()
            if emailstatus==False:
                emailstatus=True
                sum=float(sum)
		prevday=float(prevday)
		roundedprevday=round(prevday,2)
		prevday2=int(roundedprevday*100)
		roundedsum=round(sum,2)
		sum2=int(roundedsum*100)
		difference=sum2-prevday2
		difference=float(difference)/100
		#print(difference)
		#print(difference)
		difference=str(difference)
                msg = "Today you made "+str(difference)
                e = open('prevday.txt','w')
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login("", "")

                e.write(str(sum))
                e.close()
                server.sendmail("", "", msg)
                server.quit()
                print("email sent")
		driver = webdriver.Firefox()
		driver.get("https://accounts.google.com/ServiceLogin/identifier?service=grandcentral&passive=1209600&continue=https%3A%2F%2Fvoice.google.com%2Fsignup&followup=https%3A%2F%2Fvoice.google.com%2Fsignup&flowName=GlifWebSignIn&flowEntry=AddSession")
		text_area = driver.find_element_by_id('identifierId')
		text_area.send_keys("")
		text_area.send_keys(Keys.ENTER)
		time.sleep(5)
		text_area = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
		#text_area = driver.find_element_by_name('Passwd')
		text_area.send_keys("")
		text_area.send_keys(Keys.ENTER)
		time.sleep(5)
		driver.get("https://voice.google.com/u/0/messages?itemId=t.%2B18585251209")
		time.sleep(10)
		text_area = driver.find_element_by_id('input_3')
		time.sleep(5)
		text_area.send_keys("Today you made ")
		text_area.send_keys(difference)
		text_area.send_keys(Keys.ENTER)
		time.sleep(10)
		#driver.close()
		driver.close()
		print("text sent")
		prevday=sum
    sum=0
