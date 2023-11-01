#!/usr/bin/python3
"""Matrix Multiplication Function"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Raises:
        TypeError: If m_a or m_b is not a list of lists of ints/floats.
        TypeError: If m_a or m_b is empty.
        TypeError: If m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.

    Returns:
        A new matrix resulting from the multiplication of m_a and m_b.
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be lists")

    if not m_a or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not m_b or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = [[m_b[c][r] for c in range(len(m_b))] for r in range(len(m_b[0]))]

    new_matrix = [
        [
            sum(m_a[row][i] * inverted_b[col][i] for i in range(len(inverted_b[0])))
            for col in range(len(inverted_b))
        ]
        for row in range(len(m_a))
    ]

    return new_matrix
