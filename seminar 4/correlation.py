"""
Correlation
Context
Correlation is a statistical measure used to estimate
the relationship between two random variables.
● Your task
Write a script to calculate the Pearson correlation between
two random variables (two arrays). You can
use any paradigm, but I recommend using
a functional one, because in this example it will greatly
simplify your life.
● Pearson correlation formula
"""

import numpy as np


def correlation(data1, data2):
    data1 = np.array(data1)
    data2 = np.array(data2)

    def mean(data):
        return sum(data) / len(data)

    def variance(data):
        return sum((x - mean(data)) ** 2 for x in data) / len(data)

    def covariance(data1, data2):
        return sum((x1 - mean(data1)) * (x2 - mean(data2)) for (x1, x2) in zip(data1, data2)) / len(data1)

    return covariance(data1, data2) / np.sqrt(variance(data1) * variance(data2))


print(correlation([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
print(correlation([2, 3, 4, 5, 6], [5, 6, 3, 2, 4]))
