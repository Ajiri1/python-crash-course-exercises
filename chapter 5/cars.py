cars = ['bmw', 'audi', 'toyota', 'subaru']
for car in cars:
    if car == 'toyota':
        print(car.upper())
    else:
        print(car.title())

car = 'Bmw'
if car.lower() == 'bmw':
    print("True")
print(car)