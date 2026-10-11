"""Exercise 6-7: People — store three people's information in a list."""
person_1 = {
    "first_name": "Ada", "last_name": "Okafor",
    "age": 24, "city": "Port Harcourt",
}
person_2 = {
    "first_name": "Chidi", "last_name": "Nwosu",
    "age": 27, "city": "Enugu",
}
person_3 = {
    "first_name": "Mariam", "last_name": "Bello",
    "age": 22, "city": "Abuja",
}

people = [person_1, person_2, person_3]

for person in people:
    print("\nPerson:")
    for key, value in person.items():
        print(f"  {key.replace('_', ' ').title()}: {value}")
