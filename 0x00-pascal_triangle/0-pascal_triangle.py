#!/usr/bin/python3
"""Functions for generating Pascal's triangle."""


def pascal_triangle(n):
    """Generates a single row of Pascal's triangle."""
    row = [1]

    for j in range(n):
        row.append((row[j] * (n - j) // (j + 1)))

    return row


def generate_pascal_triangle(n):
    """Generates Pascal's triangle with n rows."""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        triangle.append(pascal_triangle(i + 1))

    return triangle