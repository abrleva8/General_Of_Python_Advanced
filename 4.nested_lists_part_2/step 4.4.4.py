# Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке,
# больших среднего арифметического элементов данной строки.
#
# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы (целые числа) построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести n чисел — для каждой строки количество элементов матрицы,
# больших среднего арифметического элементов данной строки.
def read_matrix(n):
    return [[int(el) for el in input().split()] for _ in range(n)]


def print_count_more_than_average(li):
    mean = sum(li) / len(li)
    return sum([el > mean for el in li])


def print_result(matrix):
    for el in matrix:
        print(print_count_more_than_average(el))


n = int(input())

matrix = read_matrix(n)
print_result(matrix)
