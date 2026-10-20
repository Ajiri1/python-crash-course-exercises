# Python Crash Course — original exercise solution
# Chapter exercise implementation; examples use Python 3.

from pathlib import Path

path = Path("learning_python.txt")
if not path.exists():
    path.write_text("I am learning Python.\nFunctions make code reusable.\nFiles preserve information.\n", encoding="utf-8")

contents = path.read_text(encoding="utf-8")
print(contents)
