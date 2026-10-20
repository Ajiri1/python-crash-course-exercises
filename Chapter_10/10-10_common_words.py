from pathlib import Path
from collections import Counter
import re

filename = input("Text file to analyze (default: learning_python.txt): ").strip()
filename = filename or "learning_python.txt"
try:
    text = Path(filename).read_text(encoding="utf-8").lower()
except FileNotFoundError:
    print(f"File not found: {filename}")
else:
    words = re.findall(r"\b[\w'-]+\b", text)
    counts = Counter(words)
    for word, count in counts.most_common(10):
        print(f"{word}: {count}")
