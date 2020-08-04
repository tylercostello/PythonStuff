from ner import Parser
import time
p = Parser()

p.load_models("models/")
def getText(file):
    with open(file, encoding="utf8") as f:
        list = f.read()
    return list
#text=getText("wpexcerpt.txt")
#text=getText("sampletextnews.txt")
#text=getText("sampleemail.txt")
#print(p.predict("Steve Went to Paris"))

def process_data(text_file, tag_file):
    with open(text_file, 'r') as f1, open(tag_file, 'r') as f2:
        sentences = f1.read().strip().split("\n")
        tags = f2.read().strip().split("\n")
        #print(tags)
        #sentences = [x.split() for x in sentences]
        tags = [x.split() for x in tags]
    return sentences,tags
sentences,tags=process_data('texta.txt','tagsa.txt')

personcounter=0
for sentence in sentences:
    #sentence=', '.join(sentence)
    #sentence=sentence.split(" ")
    output=p.predict(sentence)
    #print(sentence, end =" ")
    #for ent in doc.ents:
    #	print(ent.text, end =" ")

    for group in output:
        if ('I-PER' in group or 'B-PER' in group):
            #print(ent.text)
            personcounter+=1
            #print(group)
print(personcounter)
#3119 3.4% error
"""
start_time = time.time()
output=p.predict(text)
timeDif=(time.time() - start_time)
print(output)
print(timeDif)
"""

#0.753 sec
