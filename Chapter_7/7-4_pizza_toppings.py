"""Exercise 7-4: Pizza Toppings — accept toppings until 'quit'."""
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ").strip()
    if topping.lower() == "quit":
        break
    if topping:
        print(f"I'll add {topping} to your pizza.")
    else:
        print("Please enter a topping or type 'quit'.")
print("Your pizza order is complete.")
