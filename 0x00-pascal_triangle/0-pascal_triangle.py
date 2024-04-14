#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
    """Returns a list of lists of numbers
    representing the Pascal triangle."""
    if n <= 0:
        return []

    pascal_triangle = []

    for i in range(n):
        
        line = [0] * (i + 1)
        line[0] = 1
        line[-1] = 1
        
        
        for j in range(1, i):
            a = pascal_triangle[i - 1][j]
            b = pascal_triangle[i - 1][j - 1]
            line[j] = a + b

        pascal_triangle.append(line)

    return pascal_triangle
