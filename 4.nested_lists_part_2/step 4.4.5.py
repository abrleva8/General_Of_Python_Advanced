# Напишите программу, которая выводит максимальный элемент  квадратной матрицы ниже главной диагонали

def read_matrix(n):
    return [[int(el) for el in input().split()] for _ in range(n)]


def max_in_field(matrix):
    list_of_max = [max(matrix[i][:i + 1]) for i in range(n)]
    return max(list_of_max)

n = int(input())
matrix = read_matrix(n)
res = max_in_field(matrix)
print(res)
