"""Extra Chapter 7 examples: numeric input and a controlled while loop."""
# input() returns text, so convert numeric input before doing arithmetic.
response = input("Enter a number to double: ").strip()
try:
    number = float(response)
except ValueError:
    print("That was not a valid number.")
else:
    print(f"Double that number is {number * 2:g}.")

# Example of using continue to skip an unwanted value.
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print("Count:", count)
