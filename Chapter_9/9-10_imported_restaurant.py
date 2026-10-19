# A self-contained version demonstrating an imported class workflow.
class Restaurant:
    def __init__(self, name, cuisine):
        self.name, self.cuisine = name, cuisine

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine} food.")

if __name__ == "__main__":
    Restaurant("Harbour Kitchen", "Nigerian").describe_restaurant()
