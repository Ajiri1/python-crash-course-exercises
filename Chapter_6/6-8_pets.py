"""Exercise 6-8: Pets — store several pet dictionaries in a list."""
dog = {"name": "Bingo", "animal": "dog", "owner": "Ada"}
cat = {"name": "Milo", "animal": "cat", "owner": "Chidi"}
parrot = {"name": "Kiwi", "animal": "parrot", "owner": "Mariam"}

pets = [dog, cat, parrot]

for pet in pets:
    print(f"\nPet: {pet['name']}")
    print(f"  Animal: {pet['animal']}")
    print(f"  Owner: {pet['owner']}")
