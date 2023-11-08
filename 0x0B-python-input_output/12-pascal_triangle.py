#!/usr/bin/python3
"""Defines a pascal triangle that create a list of lists"""


def pascal_triangle(n):

    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        t = triangle[-1]
        row = [1]
        for j in range(len(t) - 1):
            row.append(t[j] + t[j + 1])
        row.append(1)
        triangle.append(row)
    return (triangle)
