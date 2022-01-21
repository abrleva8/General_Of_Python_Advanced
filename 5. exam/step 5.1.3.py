# Напишите программу, которая транспонирует квадратную матрицу.

def read_matrix(n):
    return [[int(el) for el in input().split()] for _ in range(n)]


def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print(str(el).ljust(3), end=' ')
        print()


def transpose(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


n = int(input())
matrix = read_matrix(n)
matrix = transpose(matrix)
print_matrix(matrix)
