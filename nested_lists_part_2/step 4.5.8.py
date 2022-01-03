# На шахматной доске 8×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки,
# которые бьет конь. Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь,
# отметьте символами *, остальные клетки заполните точками.

def get_number_coordinates(field : str) -> tuple:
    x_axis = 8 - int(field[1])
    y_axis = ord(field[0]) - ord('a')
    return x_axis, y_axis


def get_chess_board(size=8):
    return [['.' for _ in range(size)] for _ in range(size)]


def print_matrix(matrix):
    for row in matrix:
        print(*row)


def change_board(chess_board, field):
    x, y = field[0], field[1]
    chess_board[x][y] = 'N'
    for i in range(len(chess_board)):
        for j in range(len(chess_board)):
            if abs(x - i) * abs(y - j) == 2:
                chess_board[i][j] = '*'
    return chess_board

chess_board = get_chess_board()
field = input()
knight_field = get_number_coordinates(field)
chess_board = change_board(chess_board, knight_field)
print_matrix(chess_board)
