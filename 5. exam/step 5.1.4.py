# На вход программе подается нечетное натуральное число n.
# Напишите программу, которая создает матрицу размером n×n заполнив её символами ".".
# Затем заполните символами * среднюю строку и столбец матрицы, главную и побочную диагональ матрицы.
# Выведите полученную матрицу на экран, разделяя элементы пробелами.

def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print(str(el).ljust(3), end=' ')
        print()


def fill_matrix(n):
    def check_star(i, j, n):
        return bool(i == j or i == n - 1 - j or i == n // 2 or j == n // 2)

    return [['*' if check_star(i, j, n) else '.' for j in range(n)] for i in
            range(n)]


n = int(input())
matrix = fill_matrix(n)
print_matrix(matrix)
