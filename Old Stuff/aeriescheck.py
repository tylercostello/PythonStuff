from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import datetime
CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
WINDOW_SIZE = "1920,1080"

a = open('period1.txt','r')
b = open('period2.txt','r')
c = open('period3.txt','r')
d = open('period4.txt','r')
per1=a.read()
per2=b.read()
per3=c.read()
per4=d.read()
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
now = datetime.datetime.now()
prevminute=-1
hour=now.hour
def sendtext(msg):
	driver = webdriver.Chrome()
	driver.get("https://accounts.google.com/ServiceLogin/identifier?service=grandcentral&passive=1209600&continue=https%3A%2F%2Fvoice.google.com%2Fsignup&followup=https%3A%2F%2Fvoice.google.com%2Fsignup&flowName=GlifWebSignIn&flowEntry=AddSession")
	text_area = driver.find_element_by_id('identifierId')
	text_area.send_keys("")

	text_area.send_keys(Keys.ENTER)
	time.sleep(1)
	text_area = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
	#text_area = driver.find_element_by_name('Passwd')
	text_area.send_keys("")

	text_area.send_keys(Keys.ENTER)
	time.sleep(2)
	driver.get("https://voice.google.com/u/0/messages?itemId=t.%2B1"+"8585251209")

	time.sleep(3)
	text_area = driver.find_element_by_id('input_3')
	time.sleep(1)
	text_area.send_keys(msg)
	text_area.send_keys(Keys.ENTER)
	time.sleep(3)
	driver.close()
while hour>=6 and hour<=23:
	now = datetime.datetime.now()
	currentminute=now.minute
	if 1:
	#if currentminute==0 currentminute==30:
			if currentminute!=prevminute:
				prevminute=currentminute
				#driver = webdriver.Chrome(chrome_options=chrome_options)
				driver=webdriver.Chrome()
				driver.get('https://parent.sduhsd.net/ParentPortal/GradebookSummary.aspx')
				text_area = driver.find_element_by_id('portalAccountUsername')
				text_area.send_keys("")
				text_area.send_keys(Keys.ENTER)
				text_area = driver.find_element_by_id('portalAccountPassword')
				text_area.send_keys("")
				text_area.send_keys(Keys.ENTER)
				time.sleep(1)
				print(now)
				#print(driver.find_element_by_xpath('//*[@id="ctl00_MainContent_subGBS_DataDetails_ctl01_trGBKItem"]/td[7]/span').text)
				newper2=driver.find_element_by_xpath('//*[@id="ctl00_MainContent_subGBS_DataDetails_ctl01_trGBKItem"]/td[7]/span').text
				print(newper2)
				#print(driver.find_element_by_xpath('//*[@id="ctl00_MainContent_subGBS_DataDetails_ctl02_trGBKItem"]/td[7]/span').text)
				newper4=driver.find_element_by_xpath('//*[@id="ctl00_MainContent_subGBS_DataDetails_ctl02_trGBKItem"]/td[7]/span').text
				print(newper4)
				newper2=str(newper2)
				newper4=str(newper4)
				time.sleep(5)
				driver.close()
				if newper2!=per2:
					mymessage=" Period 2 "+str(newper2)
					sendtext(mymessage)
					b = open('period2.txt','w')
					b.write(newper2)
					per2=newper2
				if newper4!=per4:
					mymessage="Period 4 "+str(newper4)
					sendtext(mymessage)
					d = open('period4.txt','w')
					d.write(newper4)
					per4=newper4
				time.sleep(10)
