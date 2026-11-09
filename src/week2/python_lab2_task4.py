
"""
Lab 2.4 - Functional Tools Practice

Compare functional programming tools with comprehensions.
"""

PRICES = [12.5, 9.9, 15.0, 22.3, 5.0]
QUANTITIES = [2, 5, 1, 3, 4]




def item_totals(prices: list[float], quantities: list[int]) -> list[float]:

    calculated = map(
        lambda price, quantity: price * quantity,
        prices,
        quantities
    )

    return list(calculated)


def filter_above(totals: list[float], threshold: float = 30) -> list[float]:
    selected = filter(
        lambda amount: amount > threshold,
        totals
    )

    return list(selected)


def pair_up(prices: list[float], quantities: list[int]) -> list[tuple]:

    return list(zip(prices, quantities))





def item_totals_comp(prices: list[float], quantities: list[int]) -> list[float]:

    return [
        price * quantity
        for price, quantity in zip(prices, quantities)
    ]


def filter_above_comp(totals: list[float], threshold: float = 30) -> list[float]:

    return [
        amount
        for amount in totals
        if amount > threshold
    ]


if __name__ == "__main__":


    functional_totals = item_totals(PRICES, QUANTITIES)
    functional_filtered = filter_above(functional_totals)
    price_quantity_pairs = pair_up(PRICES, QUANTITIES)

    print("Totals:", functional_totals)
    print("Totals > 30:", functional_filtered)
    print("Price-quantity pairs:", price_quantity_pairs)


    comprehension_totals = item_totals_comp(PRICES, QUANTITIES)
    comprehension_filtered = filter_above_comp(comprehension_totals)

    print("Totals (comprehension):", comprehension_totals)
    print("Totals > 30 (comprehension):", comprehension_filtered)


    if functional_totals == comprehension_totals:
        print("Both approaches return identical totals.")
    else:
        print("The results are different.")

    print("List comprehensions are straightforward to read.")
