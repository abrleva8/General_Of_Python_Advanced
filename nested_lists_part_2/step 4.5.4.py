# Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.
#
# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести YES, если матрица симметрична относительно главной диагонали, и слово NO в противном случае.

def read_matrix(n):
    return [[int(el) for el in input().split()] for _ in range(n)]


def is_symmetric(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(i):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


n = int(input())
matrix = read_matrix(n)
result = is_symmetric(matrix)
print("YES" if result else "NO")