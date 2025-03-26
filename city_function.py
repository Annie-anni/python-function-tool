def get_cities(city,country,population=''):
    if population:
        cities = f"{city} {country} {population}"
    else:
        cities = f"{city} {country}"
    return cities.title()