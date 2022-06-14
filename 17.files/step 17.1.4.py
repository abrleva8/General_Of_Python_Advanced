# Вам доступен текстовый файл numbers.txt из двух строк, на каждой из них записано целое число.
# Напишите программу, выводящую на экран сумму этих чисел.

filename = 'numbers.txt'
file = open(filename, 'r', encoding='utf-8')
print(sum(map(int, file.readlines())))
file.close()
