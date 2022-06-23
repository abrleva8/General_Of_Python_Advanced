# Напишите программу, записывающую в текстовый файл random.txt 25 случайных чисел в диапазоне
# от 111 до 777 (включительно), каждое с новой строки.
import random

filename = 'random.txt'

with open(filename, 'w', encoding='utf-8') as f:
    print(*random.sample(range(111, 778), 25), sep='\n', file=f)
