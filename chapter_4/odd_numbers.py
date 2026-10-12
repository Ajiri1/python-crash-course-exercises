for values in range(1,21,2):
    print(values)

multiples = []
for value in range(3,31,3):
    multiples.append(value)

print(multiples)

cubes = []
for val in range(1,11):
    cubes.append(val**3)

print(cubes)

cubes = [va**3 for va in range(1,11)]
print(cubes)