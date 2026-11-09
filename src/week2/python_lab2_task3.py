
"""
Lab 2.3 - Operator Frequency Counter

Count arithmetic operators in a text expression.
"""

OPERATORS = ['+', '-', '*', '/', '(', ')']


def count_operators(expression: str) -> dict[str, int]:
   

    counts = dict.fromkeys(OPERATORS, 0)

    for symbol in expression:
        if symbol in counts:
            counts[symbol] += 1

    return counts


if __name__ == "__main__":

    user_expression = input("Enter an arithmetic expression: ")

    result = count_operators(user_expression)

    print("Operator counts:", result)
