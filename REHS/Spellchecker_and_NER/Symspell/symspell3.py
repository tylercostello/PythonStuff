import pkg_resources
from symspellpy import SymSpell, Verbosity
import time

sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
dictionary_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_dictionary_en_82_765.txt")
# term_index is the column of the term and count_index is the
# column of the term frequency
sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)

# lookup suggestions for single-word input strings
wordList = "memebers,tst,tast,vermnt,amzon,potat,scure,plt".split(",")

 # misspelling of "members"
# max edit distance per lookup
# (max_edit_distance_lookup <= max_dictionary_edit_distance)
start_time = time.time()
for input_term in wordList:

    suggestions = sym_spell.lookup(input_term, Verbosity.CLOSEST,
                                   max_edit_distance=2)
    # display suggestion term, term frequency, and edit distance

    for suggestion in suggestions:
        print(suggestion.term)
        break
print("--- %s seconds ---" % (time.time() - start_time))
