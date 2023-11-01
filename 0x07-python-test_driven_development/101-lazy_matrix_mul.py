#!/usr/bin/python3
"""Defines a function for lazy matrix multiplication using NumPy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Perform matrix multiplication using NumPy.
    Args:
        m_a : The first matrix.
        m_b : The second matrix.

    Returns:
        A new matrix that shows multiplication of (m_a by m_b)."""
    return np.matmul(m_a, m_b)
