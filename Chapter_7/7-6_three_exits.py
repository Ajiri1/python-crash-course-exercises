"""Exercise 7-6: Version 1 — while condition."""

topping = ""

while topping != "quit":
    topping = input("Enter a pizza topping (or 'quit' to finish): ")

    if topping != "quit":
        print(f"I'll add {topping} to your pizza.")

print("Your pizza order is complete.")






