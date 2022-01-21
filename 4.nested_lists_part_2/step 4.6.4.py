# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m
# и заполняет её числами от 1 до n⋅m в соответствии с образцом.

def fill_matrix(length: int, width: int):
    return [[j * length + i + 1 for j in range(width)] for i in range(length)]


def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print(str(el).ljust(3), end=' ')
        print()


n, m = map(int, input().split())
matrix = fill_matrix(n, m)
print_matrix(matrix)
