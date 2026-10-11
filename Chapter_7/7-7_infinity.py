"""Exercise 7-7: Infinity — demonstrate a loop that runs until interrupted.

Run this file only when you intend to stop it manually with Ctrl+C.
"""
try:
    while True:
        print("This loop keeps running. Press Ctrl+C to stop it.")
except KeyboardInterrupt:
    print("\nLoop stopped.")
