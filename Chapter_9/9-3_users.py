class User:
    def __init__(self, first_name, last_name, **details):
        self.first_name = first_name
        self.last_name = last_name
        self.details = details

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        for key, value in self.details.items():
            print(f"{key.replace('_', ' ').title()}: {value}")

    def greet_user(self):
        print(f"Welcome back, {self.first_name}!")

user = User("Favour", "Ajiri", age=20, location="Port Harcourt")
user.describe_user()
user.greet_user()
