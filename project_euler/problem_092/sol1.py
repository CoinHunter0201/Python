"""
Project Euler Problem 092: https://projecteuler.net/problem=92
Square digit chains
A number chain is created by continuously adding the square of the digits in
a number to form a new number until it has been seen before.
For example,
44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
How many starting numbers below ten million will arrive at 89?
"""


def next_number(number: int) -> int:
    """
    Returns the next number of the chain by adding the square of each digit
    to form a neww number.
    For example if number = 12, next_number() will return 1^2 + 2^2 = 5.
    Therefore 5 is the next number of the chain.
    >>> next_number(44)
    32
    >>> next_number(10)
    1
    >>> next_number(32)
    13
    """
    num = 0
    for i in range(len(str(number))):
        num += int(str(number)[i]) ** 2

    return num


def chain(number: int) -> bool:
    """
    Generates the chain of numbers until the nest number generated is 1 0r 89.
    for example, if starting number is 44, then the function generates the
    following chain of  numbers.
    chain: 44 → 32 → 13 → 10 → 1 → 1
    once the next number generated is 1 or 89, the function
    Returns True if the next number generated by next_number() if 1.
    Returns False if the next number generated by next_number() is 89.
    >>> chain(10)
    True
    >>> chain(58)
    False
    >>> chain(1)
    True
    """
    while number != 1 and number != 89:
        number = next_number(number)

    if number == 1:
        return True

    elif number == 89:
        return False


def solution(number: int = 10000000) -> int:
    """
    The function returns the total numbers that end up in 89 after the chain generation.
    The function accepts a range number and the function checks all the values
    under value number.
    if the chain generation leads to the end number as 1 or 89. If the chain()
    returns True, then total is incremented, implying that the number we
    started with ended up with 1 else total2 is incremented, implying that
    the number we started with ended up in 89 after chain generation.
    But the function returns total2 as the requirement of question is
    to find out how many ended up in 89.

    >>> solution(100)
    80
    >>> solution(10000000)
    8581146
    """
    total = 0
    total2 = 0
    for i in range(1, number):
        val = chain(i)

        if val is True:
            total += 1

        elif val is False:
            total2 += 1

    return total2


if __name__ == "__main__":
    print(f"{solution() = }")
