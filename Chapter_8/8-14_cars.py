def make_car(manufacturer, model, **details):
    car = {"manufacturer": manufacturer, "model": model}
    car.update(details)
    return car

car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)
