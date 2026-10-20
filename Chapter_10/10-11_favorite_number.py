from pathlib import Path

number = input("What is your favorite number? ").strip()
Path("favorite_number.txt").write_text(number + "\n", encoding="utf-8")
print(f"Saved favorite number: {number}")
