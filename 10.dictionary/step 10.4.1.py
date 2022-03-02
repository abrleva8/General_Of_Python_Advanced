# Программисты, как вы уже знаете, постоянно учатся, а в общении между собой используют весьма специфический язык.
# Чтобы систематизировать ваш пополняющийся профессиональный лексикон, мы придумали эту задачу. Напишите программу
# создания небольшого словаря сленговых программерских выражений,
# чтобы она потом по запросу возвращала значения из этого словаря.

n = int(input())
my_dict = {}

for _ in range(n):
    key, value = input().split(': ', 1)
    my_dict[key] = value

n = int(input())
for _ in range(n):
    print(my_dict.get(input().lower(), 'Не найдено'))
