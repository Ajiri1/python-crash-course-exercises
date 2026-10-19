"""A small example following common function style conventions."""

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"I have a {animal_type.lower()} named {pet_name.title()}.")

describe_pet("dog", "buddy")
