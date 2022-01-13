# На вход программе подаются два натуральных числа n и m.
# Напишите программу, которая создает матрицу размером n×m заполнив её "спиралью" в соответствии с образцом.


def fill_matrix(length: int, width: int):
    matrix = [[0] * width for _ in range(length)]
    count, total = 0, width * length
    i, j = 0, -1

    while count < total:
        while j + 1 < width:
            if matrix[i][j + 1] != 0:
                break
            count += 1
            j += 1
            matrix[i][j] = count

        while i + 1 < length:
            if matrix[i + 1][j] != 0:
                break
            count += 1
            i += 1
            matrix[i][j] = count

        while j - 1 >= 0:
            if matrix[i][j - 1] != 0:
                break
            count += 1
            j -= 1
            matrix[i][j] = count

        while i - 1 >= 0:
            if matrix[i - 1][j] != 0:
                break
            count += 1
            i -= 1
            matrix[i][j] = count

    return matrix


def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print(str(el).ljust(3), end=' ')
        print()


n, m = map(int, input().split())
matrix = fill_matrix(n, m)
print_matrix(matrix)
