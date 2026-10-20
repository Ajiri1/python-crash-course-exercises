class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        self.annual_salary += amount

if __name__ == "__main__":
    employee = Employee("Ada", "Lovelace", 100_000)
    print(employee.annual_salary)
    employee.give_raise()
    print(employee.annual_salary)
    employee.give_raise(10_000)
    print(employee.annual_salary)
