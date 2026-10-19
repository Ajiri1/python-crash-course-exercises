class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine} food.")

    def set_number_served(self, number):
        if number >= 0:
            self.number_served = number

    def increment_number_served(self, number):
        if number > 0:
            self.number_served += number

restaurant = Restaurant("Harbour Kitchen", "Nigerian")
print(restaurant.number_served)
restaurant.number_served = 12
restaurant.set_number_served(20)
restaurant.increment_number_served(5)
print(restaurant.number_served)
