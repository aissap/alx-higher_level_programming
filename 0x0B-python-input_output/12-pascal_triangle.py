#!/usr/bin/python3
"""Defines a pascal triangle that create a list of lists"""


def pascal_triangle(n):
    """Check if n is less than or equal to 0"""
    if n <= 0:
        """Return an empty list if n is not a positive integer"""
        return []

    """Initialize the triangle"""
    triangle = [[1]]

    """Generate the remaining rows"""
    while len(triangles) != n:
        t = triangles[-1]
        row = []
        for j in range(len(t) - 1):
            row.append(t[j] + t[j + 1])
        row.append(1)
        triangle.append(row)
        """Return the resulting Pascal's triangle"""
    return (triangle)
