# Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями:
# верхнюю, нижнюю, левую и правую.
#
# Напишите программу, которая вычисляет сумму элементов:
# верхней четверти; правой четверти; нижней четверти; левой четверти.

def read_matrix(n):
    return [[int(el) for el in input().split()] for _ in range(n)]


n = int(input())
matrix = read_matrix(n)
left_sum, right_sum, high_sum, down_sum = 0, 0, 0, 0

for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            high_sum += matrix[i][j]
        elif j > i > n - 1 - j:
            right_sum += matrix[i][j]
        elif i > j and i > n - 1 - j:
            down_sum += matrix[i][j]
        elif n - 1 - j > i > j:
            left_sum += matrix[i][j]

print(f'Верхняя четверть: {high_sum}')
print(f'Правая четверть: {right_sum}')
print(f'Нижняя четверть: {down_sum}')
print(f'Левая четверть: {left_sum}')
