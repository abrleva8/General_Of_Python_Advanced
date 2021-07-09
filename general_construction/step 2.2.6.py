# Напишите программу для определения, является ли число произведением двух чисел из данного набора,
# выводящую результат в виде ответа «ДА» или «НЕТ».
import itertools

n = int(input())
a = [int(input()) for _ in range(n)]
res = int(input())
ans = False

for num_i, num_j in itertools.combinations(a, 2):
    if num_i * num_j == res:
        ans = True
        break

print("ДА" if ans else "НЕТ")
