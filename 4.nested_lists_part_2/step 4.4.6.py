# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.

def read_matrix(n):
    return [[int(el) for el in input().split()] for _ in range(n)]


def max_in_field(matrix):
    list_of_max_1 = [max(matrix[i][:i + 1]) for i in range(n // 2)]
    list_of_max_2 = [max(matrix[i][n - i - 1:]) for i in range(n // 2)]
    list_of_max_3 = [max(matrix[i][i:]) for i in range(n // 2, n)]
    list_of_max_4 = [max(matrix[i][:n - i]) for i in range(n // 2, n)]
    max_1, max_2, max_3, max_4 = max(list_of_max_1), max(list_of_max_2), max(list_of_max_3), max(list_of_max_4)
    return max(max_1, max_2, max_3, max_4)

n = int(input())
matrix = read_matrix(n)
res = max_in_field(matrix)
print(res)
