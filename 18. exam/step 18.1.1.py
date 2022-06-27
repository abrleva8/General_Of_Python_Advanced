# На вход программе подается строка текста с именем текстового файла.
# Напишите программу для вывода на экран количества строк данного файла.

filename = input()
with open(filename, 'r', encoding='utf-8') as file:
    print(len(file.readlines()))
