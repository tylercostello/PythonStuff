from spellchecker import SpellChecker

spell = SpellChecker()
def getList(file):
    with open(file, encoding="utf8") as f:
        list = f.read().split(" ")
    return list
def lowerCaseList(upperList):
    lowerList=[x.lower().rstrip("\n") for x in upperList]
    return lowerList
#any words that you don't want flagged as misspelled can be added inside the brackets on the line below
spell.word_frequency.load_words([])
email=getList("sampleemail.txt")
email=lowerCaseList(email)
misspelled = spell.unknown(email)
for word in misspelled:
    print(word)
    print(spell.correction(word))
    print("\n")
