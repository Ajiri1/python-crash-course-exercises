from pathlib import Path

path = Path("programming_poll.txt")
print("Why do you like programming? Type q to finish.")
with path.open("a", encoding="utf-8") as file:
    while True:
        reason = input("Reason: ").strip()
        if reason.lower() == "q":
            break
        if reason:
            file.write(reason + "\n")
