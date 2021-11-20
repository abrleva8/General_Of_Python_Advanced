# На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице.
# Создайте матрицу mult размером n×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.

def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print(el.ljust(3), end=' ')
        print()

n, m = int(input()), int(input())
matrix = [[str(i * j) for j in range(m)] for i in range(n)]
print_matrix(matrix)
