#!/usr/bin/python3

"""
Pascal's Triangle
"""

def pascal_triangle(n):
    """A function that returns a list of integers
    representing Pascal triangle of n"""
    # declare pascall triangle list
    pascal_triangle = []
    # return empty list if argument == 0
    if n <= 0:
        return pascal_triangle
    for i in range(1, n+1):
        c = 1
        # declare empty inner list for each loop
        triangle_step = []
        triangle_step.append(c)
        for j in range(1, i+1):
            # combination formula
            c = c * (i - j) // j
            if c != 0:
                triangle_step.append(c)
        pascal_triangle.append(triangle_step)

    return pascal_triangle
