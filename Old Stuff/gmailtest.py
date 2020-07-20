import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#this program requires the selenium driver in your path
#A google voice account is neccessary, and you can only send messages to number which you have manually created a conversation with.
#Please replace textemail with your email, textpass with your password, and text dest with where you want it to go.
#This program also works on raspberry pi if you change it from chrome to firefox
#The delays can be shortened they were added to allow this to work on raspberry pi
#they are unneccessarily long for a normal computer
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
	driver.get("https://mail.google.com/mail/u/0/#inbox")
	time.sleep(10)
	driver.close()
sendtext("a")
