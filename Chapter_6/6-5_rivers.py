"""Exercise 6-5: Rivers — print rivers, countries, and country names."""
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "yangtze": "china",
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers in the dictionary:")
for river in rivers:
    print(river.title())

print("\nCountries in the dictionary:")
for country in rivers.values():
    print(country.title())
