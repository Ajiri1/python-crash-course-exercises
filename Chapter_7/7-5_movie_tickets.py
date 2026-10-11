"""Exercise 7-5: Movie Tickets — calculate ticket cost by age."""
while True:
    response = input("Enter your age (or 'quit' to finish): ").strip()
    if response.lower() == "quit":
        break
    try:
        age = int(response)
    except ValueError:
        print("Please enter an age as a whole number, or 'quit'.")
        continue

    if age < 0:
        print("Age cannot be negative.")
    elif age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
