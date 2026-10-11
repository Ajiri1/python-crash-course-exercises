# Python Crash Course — original exercise solution
# Chapter exercise implementation; examples use Python 3.

class Restaurant:
    def __init__(self, name, cuisine):
        self.name, self.cuisine = name, cuisine

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine} food.")

Restaurant("Harbour Kitchen", "Nigerian").describe_restaurant()
Restaurant("Pasta Place", "Italian").describe_restaurant()
Restaurant("Green Bowl", "Vegetarian").describe_restaurant()
