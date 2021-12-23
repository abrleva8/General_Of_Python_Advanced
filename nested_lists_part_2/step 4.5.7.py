# Напишите программу, которая поворачивает квадратную матрицу чисел на 90 градусов по часовой стрелке.

def read_matrix(n):
    return [[int(el) for el in input().split()] for _ in range(n)]


def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print(el, end=' ')
        print()


def transpose(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


def mirroring(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(size // 2):
            matrix[i][j], matrix[i][size - 1 - j] = matrix[i][size - 1 - j], matrix[i][j]
    return matrix


n = int(input())
matrix = read_matrix(n)
matrix = transpose(matrix)
matrix = mirroring(matrix)
print_matrix(matrix)
