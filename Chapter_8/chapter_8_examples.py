"""Chapter 8 concept examples: functions, parameters, return values, *args, **kwargs."""
def greet(name):
    print(f"Hello, {name.title()}!")

def add(a, b=0):
    return a + b

def show_items(*items):
    for item in items:
        print("-", item)

def make_profile(name, **details):
    return {"name": name, **details}

greet("favour")
print("Total:", add(4, 6))
show_items("functions", "arguments", "return values")
print(make_profile("Favour", course="Mechatronics", language="Python"))
