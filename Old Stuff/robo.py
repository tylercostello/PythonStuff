import re
from robobrowser import RoboBrowser
br = RoboBrowser(parser="lxml")
br.open('https://parent.sduhsd.net/ParentPortal/LoginParent.aspx?page=GradebookSummary.aspx')
#browser.open('https://parent.sduhsd.net/ParentPortal/LoginParent.aspx?page=GradebookSummary.aspx')
form['portalAccountUsername'].value=""
form['portalAccountPassword'].value=""
br.submit_form(form)
response = br.submit_form(form)

print(response.text)
