# Дана квадратная матрица чисел.
# Напишите программу, которая зеркально отображает её элементы относительно горизонтальной оси симметрии.

def read_matrix(n):
    return [[int(el) for el in input().split()] for _ in range(n)]


def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print(el, end=' ')
        print()


def mirroring(matrix):
    size = len(matrix)
    for i in range(size // 2):
        matrix[i], matrix[size - 1 - i] = matrix[size - 1 - i], matrix[i]
    return matrix


n = int(input())
matrix = read_matrix(n)
matrix = mirroring(matrix)
print_matrix(matrix)
