from ner import Parser
import time
p = Parser()

p.load_models("models/")
def getText(file):
    with open(file, encoding="utf8") as f:
        list = f.read()
    return list
text=getText("wpexcerpt.txt")
#text=getText("sampletextnews.txt")
#text=getText("sampleemail.txt")
#print(p.predict("Steve Went to Paris"))
start_time = time.time()
output=p.predict(text)
timeDif=(time.time() - start_time)
print(output)
print(timeDif)

#0.753 sec
