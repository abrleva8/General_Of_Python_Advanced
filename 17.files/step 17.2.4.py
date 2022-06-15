# Вам доступен текстовый файл numbers.txt, каждая строка которого может содержать одно или несколько целых чисел,
# разделенных одним или несколькими пробелами.
#
# Напишите программу, которая вычисляет сумму чисел в каждой строке и выводит эту сумму на экран
# (для каждой строки выводится сумма чисел в этой строке).

filename = 'numbers_1.txt'
with open(filename, 'r', encoding='utf-8') as file:
    data = map(lambda x: x.split(), file.read().split('\n'))

total = [sum(map(int, el)) for el in data if el]
print(*total, sep='\n')
