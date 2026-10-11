"""Exercise 7-10: Dream Vacation — collect and display a simple poll."""
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ").strip()
    place = input("If you could visit one place in the world, where would you go? ").strip()

    if name and place:
        responses[name] = place
        print(f"Thanks, {name.title()}, for responding!")
    else:
        print("Please enter both a name and a destination.")

    again = input("Would you like to let another person respond? (yes/no) ").strip().lower()
    if again != "yes":
        polling_active = False

print("\n--- Dream Vacation Poll Results ---")
if responses:
    for name, place in responses.items():
        print(f"{name.title()} would like to visit {place.title()}.")
else:
    print("No responses were recorded.")
