"""Exercise 6-10: Favorite Numbers — allow multiple numbers per person."""
favorite_numbers = {
    "Ada": [7, 14],
    "Chidi": [12, 24, 36],
    "Mariam": [3],
    "Tunde": [21, 42],
    "Zara": [9, 18],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for number in numbers:
        print(number)
