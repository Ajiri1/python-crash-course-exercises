"""Exercise 6-2: Favorite Numbers — print five people's favorite numbers."""
favorite_numbers = {
    "Ada": 7,
    "Chidi": 12,
    "Mariam": 3,
    "Tunde": 21,
    "Zara": 9,
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")#I started using the f-string method to format the output, which is more readable and efficient than concatenation.
