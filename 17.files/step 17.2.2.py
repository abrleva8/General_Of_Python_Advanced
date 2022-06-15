# Вам доступен текстовый файл data.txt, в котором записаны строки текста.
# Напишите программу, выводящую все строки данного файла в обратном порядке:
# сначала последнюю, затем предпоследнюю и т.д.

filename = 'data.txt'
with open(filename, 'r', encoding='utf-8') as file:
    print(*list(map(lambda line: line.rstrip(), file.readlines()))[::-1], sep='\n')
