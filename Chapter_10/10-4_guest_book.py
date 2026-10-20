from pathlib import Path

path = Path("guest_book.txt")
print("Enter guest names; type q to finish.")
with path.open("a", encoding="utf-8") as file:
    while True:
        name = input("Name: ").strip()
        if name.lower() == "q":
            break
        if name:
            file.write(f"{name} visited the guest book.\n")
