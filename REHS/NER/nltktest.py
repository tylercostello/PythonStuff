import time
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import tree2conlltags
def getText(file):
    with open(file, encoding="utf8") as f:
        list = f.read()
    return list
#sentence=getText("sampleemail.txt")
#sentence=getText("sampletextnews.txt")
#sentence=getText("wpexcerpt.txt")
start_time = time.time()


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
    tokens = nltk.word_tokenize(sentence)
    tagged = tree2conlltags(ne_chunk(pos_tag(tokens)))
    #print(tagged)
    #tagged = nltk.pos_tag(tokens)
    #print(tagged)
	#print(classified_text)

    for x in tagged:
        #if 'NNP' in x:
        if 'B-PERSON' in x or 'I-PERSON' in x:
            personcounter+=1
            #print(x)
timeDif=(time.time() - start_time)
print(personcounter)
#3293 9.18% error counts places and people
#17.88 sec
#print(tagged)
print(timeDif)




#0.218 sec
