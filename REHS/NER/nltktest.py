import time
import nltk
def getText(file):
    with open(file, encoding="utf8") as f:
        list = f.read()
    return list
#sentence=getText("sampleemail.txt")
#sentence=getText("sampletextnews.txt")
sentence=getText("wpexcerpt.txt")
start_time = time.time()
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
timeDif=(time.time() - start_time)

print(tagged)
print(timeDif)

#0.218 sec
