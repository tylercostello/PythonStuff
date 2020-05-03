from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://kahoot.it/')
 
thebutton = driver.find_element_by_xpath('//*[@id="mainView"]/div/div[2]/div[1]/div/form/button')
thebutton.click()
