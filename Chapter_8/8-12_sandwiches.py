def make_sandwich(*ingredients):
    print("Making a sandwich with:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich("tuna")
make_sandwich("egg", "cheese")
make_sandwich("chicken", "lettuce", "tomato", "mayonnaise")
