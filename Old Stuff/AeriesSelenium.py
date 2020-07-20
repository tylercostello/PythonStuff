from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)


driver = webdriver.Chrome(chrome_options=chrome_options)
#driver=webdriver.Chrome()
driver.get('https://parent.sduhsd.net/ParentPortal/GradebookSummary.aspx')

text_area = driver.find_element_by_id('portalAccountUsername')
text_area.send_keys("")
text_area.send_keys(Keys.ENTER)
text_area = driver.find_element_by_id('portalAccountPassword')
text_area.send_keys("")
text_area.send_keys(Keys.ENTER)
time.sleep(1)
print(driver.find_element_by_xpath('//*[@id="ctl00_MainContent_subGBS_DataDetails_ctl01_trGBKItem"]/td[7]/span').text)
print(driver.find_element_by_xpath('//*[@id="ctl00_MainContent_subGBS_DataDetails_ctl02_trGBKItem"]/td[7]/span').text)
