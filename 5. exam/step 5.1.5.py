# Напишите программу проверки симметричности квадратной матрицы относительно побочной диагонали.

def read_matrix(n):
    return [[int(el) for el in input().split()] for _ in range(n)]


def is_symmetric(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(i, size):
            if matrix[i][j] != matrix[n - j - 1][n - i - 1]:
                return False
    return True


n = int(input())
matrix = read_matrix(n)
result = is_symmetric(matrix)
print("YES" if result else "NO")
