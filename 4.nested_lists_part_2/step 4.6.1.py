# На вход программе подаются два натуральных числа n и m. Напишите программу для создания матрицы размером n×m,
# заполнив её символами . и * в шахматном порядке. В левом верхнем углу должна стоять точка.
# Выведите полученную матрицу на экран, разделяя элементы пробелами.

def get_chess_board(length, width):
    return [['.' if (i + j) % 2 == 0 else '*' for j in range(width)] for i in range(length)]


def print_matrix(matrix):
    for row in matrix:
        print(*row)


n, m = map(int, input().split())
board = get_chess_board(n, m)
print_matrix(board)
