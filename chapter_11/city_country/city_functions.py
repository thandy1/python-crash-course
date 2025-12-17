def city_functions(city_name, country_name, population=None):
    if population:
        location = f"{city_name}, {country_name} - population {population}"
    else:
        location = f"{city_name}, {country_name}"
    return location.title()