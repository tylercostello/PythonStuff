exec("""
import urllib.request
url = "https://www.wsj.com/search/term.html?KEYWORDS=baba"
f = urllib.request.urlopen(url)
print(f.read())
""")