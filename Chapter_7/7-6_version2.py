"""Exercise 7-6: Version 2 — active variable."""

active = True

while active:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")

    if topping == "quit":
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")

print("Your pizza order is complete.")
