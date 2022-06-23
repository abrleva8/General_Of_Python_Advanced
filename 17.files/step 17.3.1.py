# Напишите программу, которая считывает строку текста и записывает её в текстовый файл output.txt.

data = input()
filename = 'output.txt'
with open(filename, 'w', encoding='utf-8') as f:
    print(data, file=f)
