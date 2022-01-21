# На вход программе подается натуральное число n.
# Напишите программу, которая создает матрицу размером n×n и заполняет её по следующему правилу:
# на главной диагонали на месте каждого элемента должно стоять число 0;
# на двух диагоналях, прилегающих к главной, число 1;
# на следующих двух диагоналях число 2, и т.д.

def fill_matrix(n):
    return [[abs(int(i - j)) for j in range(n)] for i in range(n)]


def print_matrix(matrix):
    for row in matrix:
        print(*row)


n = int(input())
matrix = fill_matrix(n)
print_matrix(matrix)
