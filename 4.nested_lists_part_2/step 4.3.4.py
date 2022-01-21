# На вход программе подается натуральное число n.
# Напишите программу, которая выводит первые n строк треугольника Паскаля.

def pascal(n):
    res = [[1] * (i + 1) for i in range(n)]
    for i in range(1, n):
        for j in range(1, i):
            res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
    return res


def print_2d(li):
    for row in li:
        print(*row)


n = int(input())
res = pascal(n)
print_2d(res)
