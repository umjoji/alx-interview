#!/usr/bin/python3

"""
Pascal's Triangle
"""

from math import factorial


def pascal_triangle(n):
    """A function that returns a list of integers
    representing Pascal triangle of n"""
    p_list = []
    for i in range(1, n+1):
        c = 1
        q_list = []
        q_list.append(c)
        for j in range(1, i+1):
            c = c * (i - j) // j
            if c != 0:
                q_list.append(c)
        p_list.append(q_list)

    return p_list
