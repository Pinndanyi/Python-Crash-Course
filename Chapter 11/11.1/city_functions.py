def city_country(city, country,population = ''):
    if population:
        result = city.title() + ', ' + country.title() + "-population = " + population
    else:
        result = city.title() + ', ' + country.title()
    return result
    