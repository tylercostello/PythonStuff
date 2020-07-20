import spacy
def getText(file):
    with open(file, encoding="utf8") as f:
        list = f.read()
    return list

nlp = spacy.load('en_core_web_sm')
sentence=getText("sampleemail.txt")
#sentence = "Apple is looking at buying U.K. startup for $1 billion, while Tim Cook is also looking to buy apples from Steve Jobs"

doc = nlp(sentence)


for ent in doc.ents:
	print(ent.text, ent.start_char, ent.end_char, ent.label_)
"""
for ent in doc.ents:
	if ent.label_ == 'PERSON':
		print(ent.text, ent.start_char, ent.end_char, ent.label_)
"""
#runs into the problem distinguishing between person and country/entity
