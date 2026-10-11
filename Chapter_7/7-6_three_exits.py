"""Exercise 7-6: Three Exits — three ways to stop an input loop."""

def conditional_test_version():
    """Stop when the loop condition becomes false."""
    active = True
    while active:
        topping = input("Conditional version: topping ('quit' to stop): ").strip()
        if topping.lower() == "quit":
            active = False
        elif topping:
            print(f"I'll add {topping} to your pizza.")

def active_variable_version():
    """Use an active variable to control the loop."""
    active = True
    while active:
        age = input("Active-variable version: age ('quit' to stop): ").strip()
        if age.lower() == "quit":
            active = False
        else:
            print(f"You entered: {age}")

def break_version():
    """Exit directly with break."""
    while True:
        topping = input("Break version: topping ('quit' to stop): ").strip()
        if topping.lower() == "quit":
            break
        if topping:
            print(f"I'll add {topping} to your pizza.")

if __name__ == "__main__":
    print("Choose a version to try: 1) conditional test  2) active variable  3) break")
    choice = input("Enter 1, 2, or 3: ").strip()
    if choice == "1":
        conditional_test_version()
    elif choice == "2":
        active_variable_version()
    elif choice == "3":
        break_version()
    else:
        print("Please run the program again and choose 1, 2, or 3.")
