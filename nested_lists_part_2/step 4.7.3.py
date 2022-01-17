# Напишите программу, которая возводит квадратную матрицу в m-ую степень.

def read_matrix(n):
    return [[int(el) for el in input().split()] for _ in range(n)]


def dot_product(first_vector, second_vector):
    size = len(first_vector)
    return sum([first_vector[i] * second_vector[i] for i in range(size)])


def multiplication(first_term, second_term):
    return[[dot_product(x_col, y_col) for y_col in zip(*second_term)] for x_col in first_term]


def matrix_pow(matrix, degree):
    if degree == 1:
        return matrix

    if degree % 2 == 0:
        tmp = matrix_pow(matrix, degree//2)
        return multiplication(tmp, tmp)
    return multiplication(matrix, matrix_pow(matrix, degree - 1))


def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print(str(el).ljust(3), end=' ')
        print()


n = int(input())
matrix = read_matrix(n)
m = int(input())
matrix = matrix_pow(matrix, m)
print_matrix(matrix)
