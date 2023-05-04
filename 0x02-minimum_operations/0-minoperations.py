#!/usr/bin/python3
"""
Minimum operations task
"""


def minOperations(n):

    """
    :param n:
    :return:
    """

    if n <= 1:
        return 0
    for i in range(2, n+1):
        if n % i == 0:
            return minOperations(int(n/i)) + i
