# Напишите программу для вычисления суммы двух матриц.

def read_matrix(n):
    return [[int(el) for el in input().split()] for _ in range(n)]


def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print(str(el).ljust(3), end=' ')
        print()


def adding(first_term, second_term):
    len_1, width_1 = len(first_term), len(first_term[0])
    return[[first_term[i][j] + second_term[i][j] for j in range(width_1)] for i in range(len_1)]


n, m = map(int, input().split())
first_matrix = read_matrix(n)
input()
second_matrix = read_matrix(n)
result = adding(first_matrix, second_matrix)
print_matrix(result)
