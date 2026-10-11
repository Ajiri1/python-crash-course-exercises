# Python Crash Course — original exercise solution
# Chapter exercise implementation; examples use Python 3.

def show_magicians(names):
    for name in names:
        print(name)

def make_great(names):
    for index in range(len(names)):
        names[index] = f"the Great {names[index].title()}"
    return names

magicians = ["alice", "david", "carolina"]
great_magicians = make_great(magicians[:])
print("Original list:")
show_magicians(magicians)
print("Modified list:")
show_magicians(great_magicians)
