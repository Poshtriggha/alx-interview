#!/usr/bin/python3
"""PRINT"""


def pascal_triangle(n):
    """PRINT"""
    row = [1]

    for j in range(n):
        # define a row and fill first and last idx with 1
        row.append((row[j] * (n - j) // (j + 1)))

    return row


def print_triangle(n):
    """PRINT"""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        #Calculate the values between the first and last indices 
        triangle.append(pascal_triangle(i + 1))

    return triangle


triangle = print_triangle(5)
for row in triangle:
    print(row)