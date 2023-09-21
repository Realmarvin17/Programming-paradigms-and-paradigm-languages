"""
Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
"""


def sort_list_imperative(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


print(sort_list_imperative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))



