# Python Crash Course — original exercise solution
# Chapter exercise implementation; examples use Python 3.

def show_magicians(names):
    for name in names:
        print(name.title())

def make_great(names):
    return [f"the Great {name.title()}" for name in names]

magicians = ["alice", "david", "carolina"]
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)
