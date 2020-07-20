from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
WINDOW_SIZE = "1920,1080"
prefs = {'profile.managed_default_content_settings.images':2}
chrome_options = Options()  

chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

max=int(input("How many bots? "))
gamepin=input("What is the game pin? ")
y=0
x=0 
driver = webdriver.Chrome(chrome_options=chrome_options)

for x in range(0,max):

	y=y+1
	mystring=str(x)
	driver.get("https://kahoot.it/")
	time.sleep(0.5)
	text_area = driver.find_element_by_id('inputSession')
	text_area.send_keys(gamepin)
	text_area.send_keys(Keys.ENTER)
	time.sleep(0.5)
	text_area = driver.find_element_by_id('username')
	text_area.send_keys(mystring)
	text_area.send_keys(Keys.ENTER)
	#time.sleep(1)

	if y==6:
		driver = webdriver.Chrome(chrome_options=chrome_options)
		y=0
		time.sleep(2)
	else:
		driver.execute_script("window.open('');")
		driver.switch_to.window(driver.window_handles[y])		
time.sleep(15)
driver.quit()



