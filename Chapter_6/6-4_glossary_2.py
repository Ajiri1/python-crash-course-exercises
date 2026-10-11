"""Exercise 6-4: Glossary 2 — loop through an expanded glossary."""
glossary = {
    "variable": "A named reference to a value.",
    "string": "A sequence of characters.",
    "list": "An ordered, mutable collection of items.",
    "loop": "Code that repeats while a condition or sequence allows it.",
    "dictionary": "A collection of key-value pairs.",
    "tuple": "An ordered collection that cannot be changed after creation.",
    "boolean": "A value that is either True or False.",
    "function": "A reusable block of code that performs a task.",
    "conditional": "A statement that runs code based on a test.",
    "comment": "Text in code intended for readers, ignored by Python.",
}

for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}\n")
