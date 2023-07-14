#!/usr/bin/python3
"""
Minimum number of operations to copy
and paste a character n times
"""


def minOperations(n: int) -> int:
    """
    Calculates the fewest numbr of operations
    needed to result in exactly n characters in a file
    Returns: n(int) if possible, else 0
    """
    if n <= 1:
        return 0
    # start loop from 2 to n
    for i in range(2, n + 1):
        # if n has factors in range
        if n % i == 0:
            # recursively check for prime num & add factor
            return minOperations(int(n / i)) + i
    # if n is prime
    return n
