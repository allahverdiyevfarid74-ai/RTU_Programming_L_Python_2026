
"""
Lab 2.1 – Simple Datasets and Aggregates
Practice lists, dictionaries and tuples.
"""


def average(values: list[float]) -> float:
    if not values:
        return 0.0

    return sum(values) / len(values)


def largest_city(populations: dict[str, int]) -> tuple[str, int]:

    if not populations:
        return ("", 0)

    largest_name = ""
    largest_value = -1

    for city, population in populations.items():
        if population > largest_value:
            largest_name = city
            largest_value = population

    return (largest_name, largest_value)


def smallest_city(populations: dict[str, int]) -> tuple[str, int]:

    if not populations:
        return ("", 0)

    smallest_name = ""
    smallest_value = None

    for city, population in populations.items():
        if smallest_value is None or population < smallest_value:
            smallest_name = city
            smallest_value = population

    return (smallest_name, smallest_value) # type: ignore


def total_population(populations: dict[str, int]) -> int:
    """Calculate the combined population of all cities."""
    return sum(populations.values())


if __name__ == "__main__":


    temperatures = [8.5, 11.0, 6.5, 9.2, 12.4, 7.8, 10.6]


    city_population = {
        "Riga": 605000,
        "Daugavpils": 78000,
        "Liepaja": 67000,
        "Jelgava": 55000,
        "Ventspils": 33000
    }


    weekly_average = average(temperatures)
    biggest_city = largest_city(city_population)
    smallest_city_result = smallest_city(city_population)
    population_total = total_population(city_population)

    print(f"Average temperature: {weekly_average:.1f}")
    print(f"Largest city: {biggest_city[0]} - {biggest_city[1]}")
    print(f"Smallest city: {smallest_city_result[0]} - {smallest_city_result[1]}")
    print(f"Total population: {population_total}")
