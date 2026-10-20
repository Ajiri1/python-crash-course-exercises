from pathlib import Path

name = input("What is your name? ")
Path("guest.txt").write_text(name.strip() + "\n", encoding="utf-8")
print("Your name has been saved.")
