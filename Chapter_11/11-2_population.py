def city_country(city, country, population=None):
    result = f"{city.title()}, {country.title()}"
    if population is not None:
        result += f" - population {population}"
    return result

print(city_country("santiago", "chile"))
print(city_country("santiago", "chile", 5_000_000))
