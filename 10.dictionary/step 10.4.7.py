# Напишите программу для расшифровки секретного слова методом частотного анализа.

def get_symbol_dict(string: str) -> dict:
    my_dict = {}
    for char in string:
        my_dict[char] = my_dict.get(char, 0) + 1
    return my_dict


string = input()
n = int(input())
letters = {}
for _ in range(n):
    letter, number = input().split(': ', 1)
    letters[int(number)] = letter
symbols = get_symbol_dict(string)

for char in string:
    print(letters[symbols[char]], end='')
