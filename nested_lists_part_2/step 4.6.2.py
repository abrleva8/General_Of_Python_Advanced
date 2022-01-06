# На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n и
# заполняет её по следующему правилу:
# числа на побочной диагонали равны 1;
# числа, стоящие выше этой диагонали, равны 0;
# числа, стоящие ниже этой диагонали, равны 2.
# Полученную матрицу выведите на экран. Числа в строке разделяйте одним пробелом.

def get_weird_matrix(n):
    return [[0 if i < n - 1 - j else 1 if i == n - 1 - j else 2 for j in range(n)] for i in range(n)]


def print_matrix(matrix):
    for row in matrix:
        print(*row)


n = int(input())
matrix = get_weird_matrix(n)
print_matrix(matrix)
