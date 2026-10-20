"""Exercise 7-6: Version 3 — break statement."""

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")

    if topping == "quit":
        break

    print(f"I'll add {topping} to your pizza.")

print("Your pizza order is complete.")
