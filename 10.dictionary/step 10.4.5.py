# На вход программе подается список стран и городов каждой страны. Затем даны названия городов.
# Напишите программу, которая для каждого города выводит, в какой стране он находится.

n = int(input())
my_dict = {}
for _ in range(n):
    country, *cities = input().split()
    for city in cities:
        my_dict[city] = country

n = int(input())
for _ in range(n):
    city = input()
    print(my_dict[city])
