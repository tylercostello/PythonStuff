import smtplib
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#Please replace email user, emailpass, emaildest, textuser, textpass, and textdest with your own values
def sendemail(msg):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	#server.login(emailuser, emailpass)
	server.login("", "")
	#server.sendmail(emailuser, emaildest, msg)
	server.sendmail("", "", msg)
	server.quit()
def sendtext(msg):
	driver = webdriver.Chrome()
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
	driver.get("https://voice.google.com/u/0/messages?itemId=t.%2B1"+"8585251209")
	time.sleep(10)
	text_area = driver.find_element_by_id('input_3')
	time.sleep(5)
	text_area.send_keys(msg)
	text_area.send_keys(Keys.ENTER)
	time.sleep(30)
	driver.quit()
#sendemail("a test")
sendtext("yay robotics")
