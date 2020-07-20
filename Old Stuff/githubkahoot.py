from selenium import webdriver
import time
 
driver = webdriver.Chrome()
driver.get('https://python-forum.io/Thread-Need-Help-Opening-A-New-Tab-in-Selenium')

driver.execute_script("window.open('');")
time.sleep(3)

driver.switch_to.window(driver.window_handles[1])
driver.get("http://stackoverflow.com")
time.sleep(3)

driver.close()
time.sleep(3)

driver.switch_to.window(driver.window_handles[0])
driver.get("http://google.se")
time.sleep(3)

driver.close()