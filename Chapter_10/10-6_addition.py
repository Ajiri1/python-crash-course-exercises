try:
    first = int(input("First number: "))
    second = int(input("Second number: "))
except ValueError:
    print("Please enter valid whole numbers.")
else:
    print(f"Sum: {first + second}")
