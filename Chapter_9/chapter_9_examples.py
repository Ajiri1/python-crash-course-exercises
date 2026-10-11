"""Chapter 9 concept examples: classes, instances, inheritance, composition."""
class Car:
    def __init__(self, make, model, year):
        self.make, self.model, self.year = make, model, year
        self.odometer_reading = 0

    def describe(self):
        print(f"{self.year} {self.make.title()} {self.model.title()}")

    def read_odometer(self):
        print(f"Odometer: {self.odometer_reading} km")

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_kwh=75):
        super().__init__(make, model, year)
        self.battery_kwh = battery_kwh

car = ElectricCar("nissan", "leaf", 2024)
car.describe()
car.read_odometer()
print(f"Battery: {car.battery_kwh} kWh")
