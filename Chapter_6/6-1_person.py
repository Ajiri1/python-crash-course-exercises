"""Exercise 6-1: Person — store and print information about a person."""
person = {
    "first_name": "Ada",
    "last_name": "Okafor",
    "age": 24,
    "city": "Port Harcourt",
}

for key, value in person.items():
    print(f"{key.replace('_', ' ').title()}: {value}")
