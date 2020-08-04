def process_data(text_file, tag_file):
    with open(text_file, 'r') as f1, open(tag_file, 'r') as f2:
        sentences = f1.read().strip().split("\n")
        tags = f2.read().strip().split("\n")
        #print(tags)
        sentences = [x.split() for x in sentences]
        tags = [x.split() for x in tags]

    return sentences,tags
sentences,tags=process_data('texta.txt','tagsa.txt')
print(sentences[0])
print(tags[0])
personcounter=0
for group in tags:
    for tag in group:
        if tag=='I-PER':
            personcounter+=1
print(personcounter)
#print(tuple(process_data('texta.txt','tagsa.txt')))
#print(tuple(process_data('texta.txt','tagsa.txt')))

#3016
