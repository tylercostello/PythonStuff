import check
from symspellpy import SymSpell, Verbosity
import pkg_resources
import time
from spellchecker import SpellChecker
#The spellchecking code that I wanted to test
from functools import partial
from textblob import Word
from autocorrect import Speller
def loadFile(path):
    #assumes the format: incorrect word->correct word, alternate, alternate, ...\n
    with open(path) as f:
        d = f.read().strip()
        temp = [x.split("->") for x in d.split("\n") if "->" in d]
        for i in temp:
            #print(i)
            i[1] = i[1].split(", ")
            #print(i)
        return temp
def spellcheck(func, test):
    correctList, wrongList = [], []
    correct, total = 0, 0
    start_time = time.time()
    for word in test:
        if func(word[0]) in word[1]:
            correct += 1
            correctList.append(word)
            #print("Correct",word)
        else:
            #print(word[0],func(word[0]),word[1])
            wrongList.append(word)
            #print("Wrong", word)
        total += 1
        #if (total%10==0):
            #print(total)

    print("--- %s seconds ---" % (time.time() - start_time))
    return correct,total,correct/total
    #return correctList, wrongList, correct, total
if __name__ == "__main__":
    #Everything below should be customized to match whatever the function that is being tested needs
    pregennederrors = check.loadPreGen("variations.txt")
    test = loadFile("wikitext.txt")
    def symspell(errors, x):
        freq = check.checkWord(x, errors, 2)
        #print(freq)
        if len(freq) > 0:
            return max(freq, key=lambda x: freq[x])
        else:
            return ""
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
    spellslow = Speller()
    def autocorrecterslow(word):
        return spellslow(word)
    #print(symspell2("memebers",2))
    print("Ashwin's Symspell")
    print(spellcheck(partial(symspell, pregennederrors), test))
    print("Symspell")
    print(spellcheck(partial(symspell2), test))
    print("Autocorrect Fast")
    print(spellcheck(partial(autocorrecter), test))

    """
    Here are the other libraries, they run much slower as shown in the results below

    print("Autocorrect Slow")
    print(spellcheck(partial(autocorrecterslow), test))
    print("Spellchecker")
    print(spellcheck(partial(pyspellchecker), test))
    print("Textblob")
    print(spellcheck(partial(text_blob), test))
    """


"""
RESULTS:


Ashwin's Symspell
--- 0.2762930393218994 seconds ---
(2614, 4269, 0.6123213867416257)
Symspell
--- 1.1339364051818848 seconds ---
(3491, 4269, 0.8177559147341298)
Autocorrect Fast
--- 0.9534506797790527 seconds ---
(2978, 4269, 0.6975872569688452)
Autocorrect Slow
--- 69.29971313476562 seconds ---
(3217, 4269, 0.7535722651674865)
Spellchecker
--- 588.653124332428 seconds ---
(3385, 4269, 0.7929257437338956)
Textblob
--- 483.00193309783936 seconds ---
(2852, 4269, 0.6680721480440385)
"""