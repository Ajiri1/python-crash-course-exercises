"""Exercise 7-9: No Pastrami — remove every pastrami order before preparing."""
sandwich_orders = [
    "tuna", "pastrami", "egg salad", "pastrami",
    "chicken", "pastrami", "veggie",
]
finished_sandwiches = []

print("The deli has run out of pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nSandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")
