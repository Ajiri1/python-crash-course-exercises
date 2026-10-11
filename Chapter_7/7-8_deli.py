"""Exercise 7-8: Deli — move sandwich orders to finished_sandwiches."""
sandwich_orders = ["tuna", "pastrami", "egg salad", "chicken", "veggie"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nSandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")
