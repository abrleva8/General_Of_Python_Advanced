# На вход программе подается число n.
# Напишите программу, которая создает и выводит построчно вложенный список,
# состоящий из n списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].

n = int(input())

my_list = [[j + 1 for j in range(n)] for _ in range(n)]

for li in my_list:
    print(li)
