"""Exercise 6-11: Cities — store information about three cities."""
cities = {
    "Port Harcourt": {
        "country": "Nigeria",
        "population": "about 3 million in the urban area",
        "fact": "It is an important centre for Nigeria's oil and gas industry.",
    },
    "Tokyo": {
        "country": "Japan",
        "population": "about 14 million in the prefecture",
        "fact": "It is known for its extensive rail network.",
    },
    "Cairo": {
        "country": "Egypt",
        "population": "about 10 million in the city proper",
        "fact": "It is near the Giza pyramid complex.",
    },
}

for city, details in cities.items():
    print(f"\n{city}:")
    for key, value in details.items():
        print(f"  {key.title()}: {value}")
