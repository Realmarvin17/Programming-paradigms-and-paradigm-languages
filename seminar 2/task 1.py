"""
Multiplication table
Homework
● Condition
The input is the number n.
● Task
Write a script in any paradigm that displays a multiplication table of all numbers from 1 to n.
Justify the choice of paradigms.
● Example output:
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
..
1 * 9 = 9
"""


# Решение реализованно в виде функции в структурной парадигме, так как она является достаточно простой и понятной и
# в данном случае это лучшее решение


def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i, "*", j, "=", i * j)


print(multiplication_table(10))
