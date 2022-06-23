# На вход программе подается натуральное число n и n строк с названиями файлов.
# Напишите программу, которая создает файл output.txt
# и выводит в него содержимое всех файлов с указанными именами, не меняя их порядка.

filename_output = 'output.txt'
n = int(input())
for _ in range(n):
    filename_input = input()
    with open(filename_output, 'a', encoding='utf-8') as f_o, open(filename_input, 'r', encoding='utf-8') as f_i:
        print(f_i.read(), file=f_o)
