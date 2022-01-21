# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.

def read_matrix(n):
    return [[int(el) for el in input().split()] for _ in range(n)]


def max_in_field(matrix):
    list_of_max = [max(matrix[i][n - 1 - i:]) for i in range(n)]
    return max(list_of_max)


n = int(input())
matrix = read_matrix(n)
res = max_in_field(matrix)
print(res)
