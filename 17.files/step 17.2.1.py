# Вам доступен текстовый файл text.txt с одной строкой текста.
# Напишите программу, которая выводит на экран эту строку в обратном порядке.

filename = 'text.txt'
with open(filename) as file:
    print(file.readline().rstrip()[::-1])
