# На вход программе подается строка с именем текстового файла.
# Напишите программу, которая выводит на экран его предпоследнюю строку.

filename = input()
file = open(filename, 'r')
print(file.readlines()[-2])
file.close()
