# Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.

n = int(input())
for _ in range(n):
    print(len(set(input().lower())))
