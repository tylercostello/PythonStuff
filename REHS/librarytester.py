"""from spellchecker import SpellChecker
spell = SpellChecker()
print(spell.correction("test"))
"""
"""
from textblob import Word

word = Word('percieve')

print(word.correct())
"""
from autocorrect import Speller
spell = Speller(fast=True)
print(spell(""))
