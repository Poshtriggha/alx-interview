#!/usr/bin/python3
"""Functions for generating Pascal's triangle."""


def generate_line(n):
    """Generate a single line of Pascal's triangle."""
    line = [1]

    for i in range(n):
        line.append((line[i] * (n - i) // (i + 1)))

    return line


def generate_pascal_triangle(n):
    """Generate Pascal's triangle with n rows."""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        triangle.append(generate_line(i))

    return triangle