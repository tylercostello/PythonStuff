#warning this will use your entire ram

import spacy
import time
def getText(file):
    with open(file, encoding="utf8") as f:
        list = f.read()
    return list
#sentence=getText("wpexcerpt.txt")
#start_time = time.time()
#timeDif=(time.time() - start_time)
def process_data(text_file, tag_file):
    with open(text_file, 'r') as f1, open(tag_file, 'r') as f2:
        sentences = f1.read().strip().split("\n")
        tags = f2.read().strip().split("\n")
        #print(tags)
        #sentences = [x.split() for x in sentences]
        tags = [x.split() for x in tags]
    return sentences,tags
sentences,tags=process_data('texta.txt','tagsa.txt')
nlp = spacy.load('en_core_web_sm')
nlp.max_length = 4000000
personcounter=0
for sentence in sentences:
    #sentence=', '.join(sentence)
    doc = nlp(sentence)
    #print(sentence, end =" ")
    #for ent in doc.ents:
    #	print(ent.text, end =" ")

    for ent in doc.ents:
        if (ent.label_=='PERSON'):
            #print(ent.text)
            personcounter+=1
            for a in range(ent.text.count(" ")):
                personcounter+=1
    	#print(ent.text, ent.label_, end =" ")
    #print()

print(personcounter)


#2628 12% error


#print("Time: ",timeDif)
#0.446 sec


#runs into the problem distinguishing between person and country/entity
#Time:  117.48476076126099 for war and peace, very fast for NER
