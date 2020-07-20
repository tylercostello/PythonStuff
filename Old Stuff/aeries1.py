import mechanicalsoup
import requests
import urllib.request
from bs4 import BeautifulSoup
username=""
password=""
browser = mechanicalsoup.StatefulBrowser()
browser.open("https://parent.sduhsd.net/ParentPortal/LoginParent.aspx")
form = browser.select_form()
form.set("portalAccountUsername", username)
form.set("portalAccountPassword", password)
response = browser.submit_selected()

print(response.text)

#page = requests.get('https://parent.sduhsd.net/ParentPortal/GradebookSummary.aspx')
#print(page.text)
