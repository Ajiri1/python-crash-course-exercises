from pathlib import Path

for filename in ("cats.txt", "dogs.txt"):
    try:
        print(f"--- {filename} ---")
        print(Path(filename).read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"Could not find {filename}. Add the file and try again.")
