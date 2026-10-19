class Restaurant:
    def __init__(self, name, cuisine):
        self.name, self.cuisine = name, cuisine

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine} food.")

class IceCreamStand(Restaurant):
    def __init__(self, name, flavors):
        super().__init__(name, "ice cream")
        self.flavors = flavors

    def show_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

stand = IceCreamStand("Cool Scoops", ["vanilla", "chocolate", "strawberry"])
stand.describe_restaurant()
stand.show_flavors()
