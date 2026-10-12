"""Exercise 6-1: Person — store and print information about a person."""
person = {
    "first_name": "Ada",
    "last_name": "Okafor",
    "age": 24,
    "city": "Port Harcourt",
}

for ey, valu in person.items():
    print(ey.replace('_', ' ').title() + ": " + str(valu))
