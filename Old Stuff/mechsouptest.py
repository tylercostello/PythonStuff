

import mechanicalsoup

# Connect to duckduckgo
browser = mechanicalsoup.StatefulBrowser()
browser.open("https://parent.sduhsd.net/ParentPortal/LoginParent.aspx")

# Fill-in the search form
browser.select_form('#search_form_homepage')
browser["q"] = "MechanicalSoup"
browser.submit_selected()

# Display the results
for link in browser.get_current_page().select('a.result__a'):
    print(link.text, '->', link.attrs['href'])


browser = mechanicalsoup.StatefulBrowser()
browser.open("https://parent.sduhsd.net/ParentPortal/LoginParent.aspx")
form = browser.select_form()
form.set("portalAccountUsername")=""
form.choose_submit('form_name_attr')
browser.submit_selected()
