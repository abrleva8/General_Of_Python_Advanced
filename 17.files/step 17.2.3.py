# Вам доступен текстовый файл lines.txt, в котором записаны строки текста.
# Напишите программу, которая выводит все строки наибольшей длины из файла, не меняя их порядок.

filename = 'lines_1.txt'
with open(filename, 'r', encoding='utf-8') as file:
    data = list(map(lambda line: line.rstrip(), file.readlines()))

max_value = len(max(data, key=len))
data = filter(lambda line: len(line) == max_value, data)
print(*data, sep='\n')
