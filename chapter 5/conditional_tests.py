"""
car = "subaru"

print("Is car a subaru? I predict True.")
print(car == "subaru")

print("\nIs car a bmw? I predict False.")
print(car == "bmw")

print("\nIs car a toyota? I predict False.")
print(car == "toyota")

print("\nIs car a honda? I predict False.")
print(car == "honda")

print("\nIs car a ford? I predict False.")  
print(car == "ford")

print("\nIs car a nissan? I predict True.")
print(car != "nissan")

print("\nIs car a lambo? I predict True.")
print(car != "lambo")

print("\nIs car a bentley? I predict True.")
print(car != "bentley")

print("\nIs car a hyundai? I predict True.")
print(car != "hyundai")
"""

#Tests for equality and inequality with strings
name = "Ajiri"

print("Is your name Ajiri? I predict True.")
print(name == "Ajiri")

print("\nIs your name John? I predict False.")
print(name == "John")

#Tests using the lower() function
city = "lagos"
print("\nIs the city.lower() == 'lagos'? I predict True.")
print(city.lower() == "lagos")

print("\nIs the city.lower() == 'abuja'? I predict False.")
print(city.lower() == "abuja")

#Numerical tests
age = 25

print("\nIs age == 25? I predict True.")
print(age == 25)

print("\nIs age != 25? I predict False.")
print(age != 25)

print("\nIs age > 20? I predict True.")
print(age > 20)

print("\nIs age < 20? I predict False.")
print(age < 20)

#test using the and keyword
age = 30
print("\nIs age > 20 and age < 40? I predict True.")
print(age > 20 and age < 40)

#test using the or keyword
age = 15
print("\nIs age < 10 or age > 20? I predict False.")
print(age < 10 or age > 20)

#test whether an item is in a list
fruits = ['apple', 'banana', 'orange']
print("\nIs 'banana' in the fruits list? I predict True.")
print('banana' in fruits)

print("\nIs 'grape' in the fruits list? I predict False.")
print('grape' in fruits)

#test whether an item is not in a list
print("\nIs 'grape' not in the fruits list? I predict True.")
print('grape' not in fruits)

print("\nIs 'banana' not in the fruits list? I predict False.")
print('banana' not in fruits)