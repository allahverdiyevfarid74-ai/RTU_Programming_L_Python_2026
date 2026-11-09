
"""
Lab 2.2 - Comprehensions and Transformations

Practise list, set and dictionary comprehensions.
"""

NUMBERS = [3, 8, -2, 7, 0, -5, 10]


def squares(numbers: list[int]) -> list[int]:
    return [value * value for value in numbers]


def positives(numbers: list[int]) -> list[int]:
    return [value for value in numbers if value > 0]


def even_squares(numbers: list[int]) -> set[int]:
    return {value * value for value in numbers if value % 2 == 0}


def cubes(numbers: list[int]) -> dict[int, int]:

    return {value: value ** 3 for value in numbers}


if __name__ == "__main__":

    squared_values = squares(NUMBERS)
    positive_values = positives(NUMBERS)
    even_results = even_squares(NUMBERS)
    cube_results = cubes(NUMBERS)

    print(f"Squares: {squared_values}")
    print(f"Positives: {positive_values}")
    print(f"Even squares: {even_results}")
    print(f"Cubes: {cube_results}")
