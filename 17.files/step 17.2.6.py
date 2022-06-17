# Вам доступен текстовый файл file.txt, набранный латиницей. Напишите программу, которая выводит количество букв
# латинского алфавита, слов и строк. Выведите три найденных числа в формате, приведенном в примере.
from functools import reduce

filename = 'file.txt'
with open(filename, 'r', encoding='utf-8') as f:
    data = f.read()

l_letters = len(list(filter(str.isalpha, data)))
l_words = len(data.split())
l_lines = data.count('\n') + 1
print('Input file contains:')
print(f'{l_letters} letters')
print(f'{l_words} words')
print(f'{l_lines} lines')
