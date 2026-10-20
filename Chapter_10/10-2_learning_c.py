from pathlib import Path

path = Path("learning_python.txt")
if not path.exists():
    path.write_text("I am learning Python.\nPython is useful.\n", encoding="utf-8")

contents = path.read_text(encoding="utf-8")
print(contents.replace("Python", "C"))
