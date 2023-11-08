#!/usr/bin/python3
"""Defines a pascal triangle that create a list of lists"""


def pascal_triangle(n):
    """Check if n is less than or equal to 0"""
    if n <= 0:
        """Return an empty list if n is not a positive integer"""
        return []

    """Initialize the triangle"""
    triangle = []

    """Generate the remaining rows"""
    for i in range(n):
        row = []
        for j in range(1 + i):
            if j == 0 or j == i:
                row.append(1)
            else:
                value = triangle[i-1][j-1] + triangle[i-1][j]
                row.append(value)
        triangle.append(row)

        """Return the resulting Pascal's triangle"""
        return (triangle)
