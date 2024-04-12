#!/usr/bin/python3
"""Functions for generating Pascal's triangle."""


def generate_line(n):
    line = [1]

    for i in range(n):
        line.append((line[i] * (n - i) // (i + 1)))

    return line


def generate_pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        triangle.append(generate_line(i))

    return triangle