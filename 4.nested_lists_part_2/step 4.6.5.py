# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m
# и заполняет её числами от 1 до n⋅m в соответствии с образцом.

def fill_matrix(size: int):
    return [[1 if i == j or i == size - 1 - j else 0 for j in range(size)] for i in range(size)]


def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print(str(el).ljust(3), end=' ')
        print()


n = int(input())
matrix = fill_matrix(n)
print_matrix(matrix)
