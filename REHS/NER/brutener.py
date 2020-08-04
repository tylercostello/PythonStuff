import time
import re




start_time = time.time()
def getList(file):
    with open(file, encoding="utf8") as f:
        list = f.read()
        list=re.sub('\n', ' ', list)
        list=re.sub("\\[", ' ', list)
        list=re.sub("\\]", ' ', list)
        list=re.sub(",", ' ', list)
        list=re.sub("-", ' ', list)
        list=list.split(" ")
    return list
def lowerCaseList(upperList):
    lowerList=[x.lower() for x in upperList]
    return lowerList



namesList=set(getList("FullNamesList.txt"))
#email=getList("sampletextnews.txt")
#email=getList("26000.txt")
#email=getList("wpexcerpt.txt")
#email=lowerCaseList(email)
email=getList("texta.txt")
email=lowerCaseList(email)

removed = [x for x in email if x in namesList]
newEmail = [x for x in email if x not in namesList]
"""
print("Original: ")
print(' '.join(email))
print("With NER: ")
print(' '.join(newEmail))
print("--- %s seconds ---" % (time.time() - start_time))
"""
timeDif=(time.time() - start_time)

print(removed)
print(len(removed))
print("Time: ",timeDif)
#0.161 sec
#5209
#Misses foreign names and has problems the name list not being properly cleaned, like users picking english words as their username
