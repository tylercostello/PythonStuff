#warning this will use your entire ram

import spacy
import time
def getText(file):
    with open(file, encoding="utf8") as f:
        list = f.read()
    return list

nlp = spacy.load('en_core_web_sm')
nlp.max_length = 4000000

#sentence=getText("26000.txt")
#sentence=getText("sampleemail.txt")
#sentence=getText("sampletextnews.txt")
sentence=getText("wpexcerpt.txt")
#sentence = "Apple is looking at buying U.K. startup for $1 billion, while Tim Cook is also looking to buy apples from Steve Jobs"


start_time = time.time()
doc = nlp(sentence)
timeDif=(time.time() - start_time)


for ent in doc.ents:
	print(ent.text, ent.start_char, ent.end_char, ent.label_)
"""
for ent in doc.ents:
	if ent.label_ == 'PERSON' or ent.label_ == 'GPE':
		print(ent.text, ent.start_char, ent.end_char, ent.label_)
"""

print("Time: ",timeDif)
#0.446 sec


#runs into the problem distinguishing between person and country/entity
#Time:  117.48476076126099 for war and peace, very fast for NER
