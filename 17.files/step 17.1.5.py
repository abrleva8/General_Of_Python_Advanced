# Вам доступен текстовый файл nums.txt.
# В файле записано два целых числа, они могут быть разделены символами пробела и конца строки.
# Напишите программу, выводящую на экран сумму этих чисел.

filename = 'nums.txt'
file = open(filename, 'r', encoding='utf-8')
print(sum(map(int, filter(None, map(lambda line: line.strip(), file.readlines())))))
file.close()
