# Латинским квадратом порядка n называется квадратная матрица размером n×n,
# каждая строка и каждый столбец которой содержат все числа от 1 до n.
# Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.

def read_matrix(n):
    return [[int(el) for el in input().split()] for _ in range(n)]


def check_list(row, size):
    li = list(range(1, size + 1))
    for el in row:
        if el in li:
            li.remove(el)
        else:
            return False
    return True


def check_row(matrix):
    size = len(matrix)
    for row in matrix:
        if not check_list(row, size):
            return False
    return True


def check_col(matrix):
    size = len(matrix)
    for y_col in zip(*matrix):
        if not check_list(y_col, size):
            return False
    return True


def is_latin(matrix):
    is_row_good = check_row(matrix=matrix)
    is_col_good = check_col(matrix=matrix)
    return is_row_good and is_col_good


size = int(input())
matrix = read_matrix(size)
print("YES" if is_latin(matrix) else "NO")
