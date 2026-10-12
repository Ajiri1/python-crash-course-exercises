motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(1, 'hybrid')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

first = motorcycles.pop(1)
print("the first motorcycle I owned was a " + first.title() + ".")

motorcycles = ['yamaha', 'honda', 'ducati', 'suzuki']
motorcycles.remove('ducati')
print(motorcycles)

too_expensive = 'honda'
motorcycles.remove(too_expensive)
print(motorcycles)
print("A " + too_expensive.title() + " is too expensive for me.")

name = ['junior', 'jason', 'junior', 'jasper']
name.remove('junior')
print(name)
