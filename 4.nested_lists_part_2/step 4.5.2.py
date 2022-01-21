# На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице,
# затем n строк по m целых чисел в каждой, отделенных символом пробела.
#
# Напишите программу, которая находит индексы (строку и столбец) первого вхождения максимального элемента.

def read_matrix(n):
    return [[int(el) for el in input().split()] for _ in range(n)]


def find_maximum(matrix):
    maximum, i_max, j_max = matrix[0][0], 0, 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > maximum:
                maximum, i_max, j_max = matrix[i][j], i, j
    return i_max, j_max


n, m = int(input()), int(input())
matrix = read_matrix(n)
max_index = find_maximum(matrix)
print(*max_index)
