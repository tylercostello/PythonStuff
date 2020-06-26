from spellchecker import SpellChecker

def getList(file):
    with open(file, encoding="utf8") as f:
        list = f.read().split(" ")
    return list
def lowerCaseList(upperList):
    lowerList=[x.lower().rstrip("\n") for x in upperList]
    return lowerList

spell = SpellChecker()
#add words you don't want flagged inside the brackets
spell.word_frequency.load_words(['google'])
email=getList("sample.txt")
email=lowerCaseList(email)
misspelled = spell.unknown(email)
print("Original: ")
print(email)
print("Misspelled words and corrections: ")
for word in misspelled:
    print(word)
    print(spell.correction(word))
    print("\n")
