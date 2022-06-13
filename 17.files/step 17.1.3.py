# Вам доступен текстовый файл lines.txt из нескольких строк. Напишите программу,
# которая выводит на экран случайную строку из этого файла.

import random

filename = 'lines.txt'
file = open(filename, 'r', encoding='utf-8')
lines = file.readlines()
file.close()
print(random.choice(lines).rstrip())
