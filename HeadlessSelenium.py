exec("""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#CHROME_PATH = '/usr/bin/google-chrome'
#CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
#WINDOW_SIZE = "1920,1080"

chrome_options = Options()  
#chrome_options.add_argument("--headless")  
#chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
driver = webdriver.Chrome(chrome_options=chrome_options)  
driver.get('https://python.org/')
 
html = driver.page_source
print(html)
driver.close()
""")
