# Напишите программу, которая меняет местами столбцы в матрице.

# На вход программе на разных строках подаются два натуральных числа n и m — количество строк и столбцов в матрице,
# затем элементы матрицы построчно через пробел, затем числа i и j — номера столбцов, подлежащих обмену.

def read_matrix(n):
    return [input().split() for _ in range(n)]


def swap(matrix, i, j):
    for row in matrix:
        row[i], row[j] = row[j], row[i]
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print(el.ljust(3), end=' ')
        print()


n, m = int(input()), int(input())
matrix = read_matrix(n)
i, j = map(int, input().split())
matrix = swap(matrix=matrix, i=i, j=j)
print_matrix(matrix)
