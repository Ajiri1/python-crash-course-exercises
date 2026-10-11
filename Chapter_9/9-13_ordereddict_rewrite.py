# Python Crash Course — original exercise solution
# Chapter exercise implementation; examples use Python 3.

from collections import OrderedDict

glossary = OrderedDict([
    ("list", "An ordered collection of items."),
    ("dictionary", "A collection of key-value pairs."),
    ("function", "A reusable block of code."),
    ("loop", "Code that repeats while iterating or a condition holds."),
])
for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}")
