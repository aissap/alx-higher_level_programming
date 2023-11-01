#!/usr/bin/python3
"""Defines a matrix division """


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    Args:
        matrix : A list of lists of ints or floats.
        div :The divisor.
    Raises:
        TypeError: contains non-numbers or div is not an int or float.
        TypeError: contains rows of different sizes.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix contains the result of the division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(element, int) or isinstance(element, float))
                    for row in matrix for element in row)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
