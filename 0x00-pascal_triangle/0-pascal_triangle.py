#!/usr/bin/python3
"""PRINT"""


def pascal_triangle(n):
    """PRINT"""
    row = [1]

    for j in range(n):
        row.append((row[j] * (n - j) // (j + 1)))

    return row


def print_triangle(n):
    """PRINT"""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        triangle.append(pascal_triangle(i + 1))

    return triangle


triangle = print_triangle(5)
for row in triangle:
    print(row)