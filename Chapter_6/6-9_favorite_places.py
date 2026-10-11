"""Exercise 6-9: Favorite Places — print each person's favorite places."""
favorite_places = {
    "Ada": ["Obudu Mountain Resort", "Lagos"],
    "Chidi": ["Enugu", "Calabar", "Yankari"],
    "Mariam": ["Zanzibar"],
}

for name, places in favorite_places.items():
    print(f"{name}'s favorite places are:")
    for place in places:
        print(f"  - {place}")
