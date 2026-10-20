from pathlib import Path

for filename in ("cats.txt", "dogs.txt"):
    try:
        print(Path(filename).read_text(encoding="utf-8"))
    except FileNotFoundError:
        pass  # Deliberately ignore a missing file for this exercise.
