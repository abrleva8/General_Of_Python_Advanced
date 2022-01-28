# Напишите программу, которая выводит список хорошистов и отличников в классе.

n = int(input())

data = []

for _ in range(n):
    s = input()
    print(s)
    data.append(s)

print()

for name in data:
    name_list = name.split()
    if int(name_list[1]) > 3:
        print(name)
