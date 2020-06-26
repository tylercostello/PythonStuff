def getList(file):
    with open(file, encoding="utf8") as f:
        list = f.read().split(" ")
    return list
def lowerCaseList(upperList):
    lowerList=[x.lower().rstrip("\n") for x in upperList]
    return lowerList

namesList=[]

namesList+=getList("FullNamesList.txt")

email=getList("sample.txt")
email=lowerCaseList(email)
newEmail = [x for x in email if x not in namesList]
print("Original: ")
print(email)
print("With NER: ")
print(newEmail)
