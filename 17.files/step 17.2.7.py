# Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами, другой с фамилиями.
#
# Напишите программу, которая c помощью модуля random создает 3 случайные пары имя + фамилия,
# а затем выводит их, каждую на отдельной строке.
import random

filename_first, filename_last = 'first_names.txt', 'last_names.txt'
with open(filename_first, 'r', encoding='utf-8') as f_first, open(filename_last, 'r', encoding='utf-8') as f_last:
    first_names = f_first.read().split()
    last_names = f_last.read().split()

for _ in range(3):
    print(f'{random.choice(first_names)} {random.choice(last_names)}')
