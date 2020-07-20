#mailbox stuff
import requests

#read function
url="http://submitthing.000webhostapp.com/mytextfile.txt"
page = requests.get(url)
text=str(page.text.encode('utf8'))
print(text[2])

#write function
#requests.post('http://submitthing.000webhostapp.com/action.php', data={'age':'5'})
