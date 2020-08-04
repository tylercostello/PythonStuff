from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import time
st = StanfordNERTagger('stanford-ner-4.0.0/classifiers/english.all.3class.distsim.crf.ser.gz',
					   'stanford-ner-4.0.0/stanford-ner-4.0.0.jar',
					   encoding='utf-8')
def getText(file):
    with open(file, encoding="utf8") as f:
        list = f.read()
    return list
#text=getText("sampletextnews.txt")
#text=getText("wpexcerpt.txt")
#text=getText("sampleemail.txt")
#text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'
#start_time = time.time()
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
	tokenized_text = word_tokenize(sentence)
	classified_text = st.tag(tokenized_text)
	#print(classified_text)

	for x in classified_text:
		if 'PERSON' in x:
			personcounter+=1
	print(personcounter)
#2403 20% error


#timeDif=(time.time() - start_time)
#print(classified_text)
#print(timeDif)


#2.710 sec
