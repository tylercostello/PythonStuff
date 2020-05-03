import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
WINDOW_SIZE = "1920,1080"
prefs = {'profile.managed_default_content_settings.images':2}
chrome_options = Options()

chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
#driver = webdriver.Chrome()
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://accounts.google.com/signin/v2/identifier?service=grandcentral&passive=1209600&continue=https%3A%2F%2Fvoice.google.com%2Fsignup&followup=https%3A%2F%2Fvoice.google.com%2Fsignup&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
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
text_area.send_keys("Hello Chula Vista 2!")
text_area.send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()
