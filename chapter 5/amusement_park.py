"""
age = int(input("Please enter your age: "))
if age < 4:
    print("Your admission cost is $0.")
elif age >= 4 and age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
"""

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age >= 18:
    price = 10
else:
    price = 70
print("Your admission cost is $" + str(price) + ".")


