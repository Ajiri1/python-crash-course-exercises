age = int(input("Please enter your age: "))
if age >= 18:
    print("You are old enough to vote.")
    print("Have you registered to vote yet?")
    ajiri = input("Please enter your voter registration information: ")
    print("Thank you for registering to vote! " + ajiri)
else:
    print("You are not old enough to vote.")
    print("Please register to vote as soon as you turn 18!")

