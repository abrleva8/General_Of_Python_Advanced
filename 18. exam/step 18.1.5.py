# На вход программе подается строка текста с именем текстового файла.
# Напишите программу, выводящую на экран последние 10 строк данного файла.

filename = input()
with open(filename, 'r', encoding='utf-8') as file:
    print(*map(lambda x: x.rstrip(), file.readlines()[-10:]), sep='\n')
