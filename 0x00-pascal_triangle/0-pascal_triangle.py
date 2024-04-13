#!/usr/bin/python3
"""Functions for generating Pascal's triangle."""


def generate_pascal_triangle(n):
    """
    Generate Pascal's triangle with the specified number of rows.

    Parameters:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # first element of the row
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])  # middle elements
        new_row.append(1)  # last element of the row
        triangle.append(new_row)

    return triangle
