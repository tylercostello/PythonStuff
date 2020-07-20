import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

msg=input("What is your message? ")
destination=input("Where do you want it sent? ")
driver = webdriver.Chrome()

driver.get("https://accounts.google.com/ServiceLogin/identifier?service=grandcentral&passive=1209600&continue=https%3A%2F%2Fvoice.google.com%2Fsignup&followup=https%3A%2F%2Fvoice.google.com%2Fsignup&flowName=GlifWebSignIn&flowEntry=AddSession")
text_area = driver.find_element_by_id('identifierId')
text_area.send_keys("")
text_area.send_keys(Keys.ENTER)
time.sleep(3)
text_area = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
#text_area = driver.find_element_by_name('Passwd')
text_area.send_keys("")
text_area.send_keys(Keys.ENTER)
time.sleep(3)
driver.get("https://voice.google.com/u/0/messages?itemId=t.%2B1"+destination)
time.sleep(3)
text_area = driver.find_element_by_id('input_3')
time.sleep(2)
text_area.send_keys(msg)
text_area.send_keys(Keys.ENTER)
