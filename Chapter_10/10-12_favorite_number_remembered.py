from pathlib import Path

path = Path("favorite_number.txt")
if path.exists():
    print(f"I know your favorite number! It is {path.read_text(encoding='utf-8').strip()}.")
else:
    number = input("What is your favorite number? ").strip()
    path.write_text(number + "\n", encoding="utf-8")
    print("I'll remember that next time.")
