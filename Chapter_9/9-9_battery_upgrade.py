# Python Crash Course — original exercise solution
# Chapter exercise implementation; examples use Python 3.

class Battery:
    def __init__(self, size=75):
        self.size = size

    def describe_battery(self):
        print(f"This car has a {self.size}-kWh battery.")

    def upgrade(self):
        if self.size < 100:
            self.size = 100

class ElectricCar:
    def __init__(self, make, model, year):
        self.make, self.model, self.year = make, model, year
        self.battery = Battery()

car = ElectricCar("Nissan", "Leaf", 2024)
car.battery.describe_battery()
car.battery.upgrade()
car.battery.describe_battery()
