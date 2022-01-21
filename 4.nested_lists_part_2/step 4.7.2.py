# Напишите программу, которая перемножает две матрицы.

def read_matrix(n):
    return [[int(el) for el in input().split()] for _ in range(n)]


def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print(str(el).ljust(3), end=' ')
        print()


def dot_product(first_vector, second_vector):
    size = len(first_vector)
    return sum([first_vector[i] * second_vector[i] for i in range(size)])


def multiplication(first_term, second_term):
    return[[dot_product(x_col, y_col) for y_col in zip(*second_term)] for x_col in first_term]


n, _ = map(int, input().split())
first_matrix = read_matrix(n)
input()
n, _ = map(int, input().split())
second_matrix = read_matrix(n)
result = multiplication(first_matrix, second_matrix)
print_matrix(result)
