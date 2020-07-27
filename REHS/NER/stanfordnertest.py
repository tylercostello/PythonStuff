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
text=getText("wpexcerpt.txt")
#text=getText("sampleemail.txt")
#text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'
start_time = time.time()
tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)
timeDif=(time.time() - start_time)
print(classified_text)
print(timeDif)


#2.710 sec
