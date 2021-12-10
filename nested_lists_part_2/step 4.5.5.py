# Дана квадратная матрица чисел.Напишите программу, которая меняет местами элементы, стоящие на главной
# и побочной диагонали, при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце нужно
# поменять местами элемент на главной диагонали и на побочной диагонали).

def read_matrix(n):
    return [[int(el) for el in input().split()] for _ in range(n)]


def exchange_of_the_diagonals(matrix):
    size = len(matrix)
    for i in range(size):
        matrix[i][i], matrix[size - i - 1][i] = matrix[size - i - 1][i], matrix[i][i]
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print(el, end=' ')
        print()


n = int(input())
matrix = read_matrix(n)
matrix = exchange_of_the_diagonals(matrix)
print_matrix(matrix)
