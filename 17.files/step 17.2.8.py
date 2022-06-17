# Вам доступен текстовый файл population.txt с названиями стран и численностью их населения,
# разделенными символом табуляции '\t'.
#
# Напишите программу выводящую все страны, название которых начинается с буквы 'G',
# численность населения которых больше чем 500000 человек, не меняя их порядок.

filename = 'population.txt'

with open(filename, 'r', encoding='utf-8') as f:
    cities = map(lambda x: x.split('\t')[0], filter(lambda x: x.startswith('G') and int(x.split('\t')[1]) > 500000,
                                                    f.read().split('\n')))
print(*cities, sep='\n')
