# Вам доступен текстовый файл class_scores.txt с оценками за итоговый тест на строках вида:
# фамилия оценка (фамилия и оценка разделены пробелом). Оценка - целое число от 0 до 100 включительно.
#
# Напишите программу для добавления 5 баллов к каждому результату теста и вывода фамилии
# и новых результатов тестов в файл new_scores.txt.

filename_input = 'class_scores.txt'
filename_output = 'new_scores.txt'

with open(filename_input, 'r', encoding='utf-8') as f_i:
    results = f_i.readlines()

with open(filename_output, 'w', encoding='utf-8') as f_o:
    for line in results:
        data = line.split()
        print(f'{data[0]} {min(100, int(data[1]) + 5)}', file=f_o)

