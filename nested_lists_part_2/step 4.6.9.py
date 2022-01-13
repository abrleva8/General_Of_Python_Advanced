# На вход программе подаются два натуральных числа n и m.
# Напишите программу, которая создает матрицу размером n×m заполнив её "диагоналями" в соответствии с образцом.


def fill_matrix(length: int, width: int):

    def fill_diag(matrix, i, j, start_value):
        length, width = len(matrix), len(matrix[0])
        while 0 <= i < length and 0 <= j < width:
            matrix[i][j] = start_value
            start_value += 1
            i += 1
            j -= 1
        return matrix, start_value

    num = 1
    matrix = [[0] * width for _ in range(length)]

    for j in range(width):
        matrix, num = fill_diag(matrix, 0, j, num)

    for i in range(1, length):
        matrix, num = fill_diag(matrix, i, width - 1, num)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print(str(el).ljust(3), end=' ')
        print()


n, m = map(int, input().split())
matrix = fill_matrix(n, m)
print_matrix(matrix)
