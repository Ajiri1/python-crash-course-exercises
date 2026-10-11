"""Exercise 6-3: Glossary — define five programming terms."""
glossary = {
    "variable": "A named reference to a value.",
    "string": "A sequence of characters.",
    "list": "An ordered, mutable collection of items.",
    "loop": "Code that repeats while a condition or sequence allows it.",
    "dictionary": "A collection of key-value pairs.",
}

for word, meaning in glossary.items():
    print(f"{word.title()}:")
    print(f"  {meaning}\n")
