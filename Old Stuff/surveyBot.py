
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui, time
#CHROME_PATH = '/usr/bin/google-chrome'
#CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
#WINDOW_SIZE = "1920,1080"

chrome_options = Options()  

driver = webdriver.Chrome(chrome_options=chrome_options)  
#driver.get('https://docs.google.com/forms/d/1yfNqyqKbvBj3o7umLhp03y7v1UgC4eidsoCL1PSm6zk/viewform?edit_requested=true')
driver.get('https://docs.google.com/forms/d/1LJ5T_BSnxOh1bGDEKTFSsCmIWxnKKSZGgJ9L79m9ewc/viewform?edit_requested=true')
for x in range (0,10000):
    pyautogui.typewrite(['tab','tab','down','tab','down','tab','down','tab','down','tab','down','tab','down','tab'],0.25)
    pyautogui.typewrite('1', 0.25)
    pyautogui.typewrite(['tab','down','tab','down','tab','space'],0.25)
    pyautogui.typewrite(['tab','tab','tab','tab','tab','tab','tab','tab','tab','space','tab','tab','tab','tab','tab','tab','tab','space','tab','tab','tab','tab','tab','enter'],0.25)
    #time.sleep(5)
    driver.get('https://docs.google.com/forms/d/1LJ5T_BSnxOh1bGDEKTFSsCmIWxnKKSZGgJ9L79m9ewc/viewform?edit_requested=true')
    #time.sleep(5)
    print(x)
driver.close()


