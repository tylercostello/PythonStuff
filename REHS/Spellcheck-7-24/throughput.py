from symspellpy import SymSpell, Verbosity
import pkg_resources
import time
from spellchecker import SpellChecker
from functools import partial
from textblob import Word
from autocorrect import Speller

def getText(file):
    with open(file, encoding="utf8") as f:
        list = f.read()
    return list

def getList(file):
    with open(file, encoding="utf8") as f:
        list = f.read().split(" ")
    return list
def lowerCaseList(upperList):
    lowerList=[x.lower().rstrip("\n") for x in upperList]
    return lowerList



sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
dictionary_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_dictionary_en_82_765.txt")

sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
def symspell2(word):
    input_term = word
    suggestions = sym_spell.lookup(input_term, Verbosity.CLOSEST,
                                   max_edit_distance=2)
    for suggestion in suggestions:
        return suggestion.term
spell1 = SpellChecker()
def pyspellchecker(word):
    return spell1.correction(word)
def text_blob(word):
    return Word(word).correct()
spell = Speller(fast=True)
def autocorrecter(word):
    return spell(word)



#text=getList("62668-0.txt")
#text=getList("moby10b.txt")
#text=getList("largetext.txt")
text=getList("0100011.txt")
#text=getList("26000.txt")
text=lowerCaseList(text)
print("Words",len(text))


start_time = time.time()
for word in text:
    symspell2(word)
runningTime=(time.time() - start_time)
print("Symspell")
print("Seconds",runningTime)
print("Words per second:", len(text)/runningTime )


start_time = time.time()
for word in text:
    autocorrecter(word)
runningTime=(time.time() - start_time)
print("Autocorrect")
print("Seconds",runningTime)
print("Words per second:", len(text)/runningTime )

#The other 2 libraries run too slow, about 10 words per second, to include in this test
#Here is the code to run them if you ever want to run the other libraries but you should probably use a different text file

"""
start_time = time.time()
for word in text:
    pyspellchecker(word)
runningTime=(time.time() - start_time)
print("Seconds",runningTime)
print("Words per second:", len(text)/runningTime )

start_time = time.time()
for word in text:
    text_blob(word)
runningTime=(time.time() - start_time)
print("Seconds",runningTime)
print("Words per second:", len(text)/runningTime )
"""



"""
RESULTS

Words 517025

Symspell
Seconds 42.576579570770264
Words per second: 12143.413238271229

Autocorrect
Seconds 6.239381313323975
Words per second: 82864.78643257653

the other 2 run about 10 words per second so they would take too long to run
their comparative speed can be seen in AccuracyTester.py

"""
