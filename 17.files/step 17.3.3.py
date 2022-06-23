# Вам доступен текстовый файл input.txt, состоящий из нескольких строк.
# Напишите программу для записи содержимого этого файла в файл output.txt в виде нумерованного списка,
# где перед каждой строкой стоит ее номер, символ ) и пробел. Нумерация строк должна начинаться с 1.

filename_input = 'input.txt'
filename_output = 'output.txt'

with open(filename_input, 'r', encoding='utf-8') as f_i, open(filename_output, 'w', encoding='utf-8') as f_o:
    for index, line in enumerate(f_i.readlines()):
        print(f'{index + 1}) {line}', file=f_o, end='')
