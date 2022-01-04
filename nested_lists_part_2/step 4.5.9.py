# Магическим квадратом порядка nn называется квадратная таблица размера n×n, составленная из всех чисел 1,2,3, …,n^2
# так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой.
# Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.

def read_matrix(n):
    return [[int(el) for el in input().split()] for _ in range(n)]


def check_numbers(matrix):
    size = len(matrix)
    li = list(range(1, size * size + 1))
    for i in range(size):
        for j in range(size):
            if matrix[i][j] in li:
                li.remove(matrix[i][j])
            else:
                return False
    return True


def check_row_sum(matrix, check_sum):
    for row in matrix:
        if sum(row) != check_sum:
            return False
    return True


def check_col_sum(matrix, check_sum):
    for i in range(len(matrix)):
        if sum([matrix[j][i] for j in range(len(matrix))]) != check_sum:
            return False
    return True


def check_track(matrix, check_sum):
    size = len(matrix)
    if sum([matrix[i][i] for i in range(size)]) != check_sum:
        return False
    elif sum([matrix[size - i - 1][i] for i in range(size)]) != check_sum:
        return False
    return True


def is_magic(matrix):
    size = len(matrix)
    check_sum = size * (size * size + 1) / 2
    is_row_good = check_row_sum(matrix=matrix, check_sum=check_sum)
    is_col_good = check_col_sum(matrix=matrix, check_sum=check_sum)
    is_diag_good = check_track(matrix=matrix, check_sum=check_sum)
    return is_row_good and is_col_good and is_diag_good and check_numbers(matrix)


size = int(input())
matrix = read_matrix(size)
print("YES" if is_magic(matrix) else "NO")
