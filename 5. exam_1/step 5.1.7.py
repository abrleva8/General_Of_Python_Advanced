# На шахматной доске 8×8 стоит ферзь. Отметьте положение ферзя на доске и все клетки, которые бьет ферзь.
# Клетку, где стоит ферзь, отметьте буквой Q, клетки, которые бьет ферзь,
# отметьте символами *, остальные клетки заполните точками.

def get_number_coordinates(field : str) -> tuple:
    x_axis = 8 - int(field[1])
    y_axis = ord(field[0]) - ord('a')
    return x_axis, y_axis


def get_chess_board(size=8):
    return [['.' for _ in range(size)] for _ in range(size)]


def change_board(chess_board, field):
    x, y = field[0], field[1]
    chess_board[x][y] = 'Q'
    for i in range(len(chess_board)):
        for j in range(len(chess_board)):
            if x == i or y == j or abs(x - i) == abs(y - j):
                chess_board[i][j] = '*'
    chess_board[x][y] = 'Q'
    return chess_board


def print_matrix(matrix):
    for row in matrix:
        print(*row)


chess_board = get_chess_board()
field = input()
queen_field = get_number_coordinates(field)
chess_board = change_board(chess_board, queen_field)
print_matrix(chess_board)
