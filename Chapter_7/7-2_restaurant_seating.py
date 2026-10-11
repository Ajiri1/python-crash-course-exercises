"""Exercise 7-2: Restaurant Seating — check the size of the dinner group."""
try:
    people = int(input("How many people are in your dinner group? "))
    if people < 1:
        print("Please enter a positive number of people.")
    elif people > 8:
        print("You'll have to wait for a table.")
    else:
        print("Your table is ready.")
except ValueError:
    print("Please enter a whole number.")
