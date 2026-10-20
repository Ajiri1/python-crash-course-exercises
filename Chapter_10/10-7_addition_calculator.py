print("Addition calculator; type q to quit.")
while True:
    first = input("First number: ")
    if first.lower() == "q":
        break
    second = input("Second number: ")
    if second.lower() == "q":
        break
    try:
        total = int(first) + int(second)
    except ValueError:
        print("Please enter whole numbers.")
    else:
        print(f"Sum: {total}")
