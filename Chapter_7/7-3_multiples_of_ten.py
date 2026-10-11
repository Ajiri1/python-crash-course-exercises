"""Exercise 7-3: Multiples of Ten — check divisibility by 10."""
try:
    number = int(input("Enter a number: "))
    if number % 10 == 0:
        print(f"{number} is a multiple of 10.")
    else:
        print(f"{number} is not a multiple of 10.")
except ValueError:
    print("Please enter a whole number.")
