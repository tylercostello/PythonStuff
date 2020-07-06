import check
from symspellpy import SymSpell, Verbosity
import pkg_resources
import time

#The spellchecking code that I wanted to test
from functools import partial
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
    #print(symspell2("memebers",2))
    print(spellcheck(partial(symspell, pregennederrors), test))
    print(spellcheck(partial(symspell2), test))
