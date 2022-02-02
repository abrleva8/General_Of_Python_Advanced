# Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.

n = int(input())
symbols = set()
for _ in range(n):
    symbols = symbols.union(set(input().lower()))
print(len(symbols))
