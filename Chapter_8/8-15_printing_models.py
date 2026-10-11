# Python Crash Course — original exercise solution
# Chapter exercise implementation; examples use Python 3.

# This exercise practices importing functions from a separate module.
# Run this file together with printing_functions.py in the same folder.

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        completed_models.append(unprinted_designs.pop())

def show_completed_models(completed_models):
    print("Completed models:")
    for model in completed_models:
        print(model)

if __name__ == "__main__":
    designs = ["phone case", "robot pendant", "dodecahedron"]
    completed = []
    print_models(designs[:], completed)
    show_completed_models(completed)
