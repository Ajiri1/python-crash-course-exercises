"""Exercise 7-1: Rental Car — ask what car the user wants."""
car = input("What kind of rental car would you like? ").strip()
if car:
    print(f"Let me see if I can find you a {car.title()}.")
else:
    print("You didn't enter a car type.")
