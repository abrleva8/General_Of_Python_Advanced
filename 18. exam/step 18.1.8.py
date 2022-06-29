# При написании собственных функций рекомендуется в комментарии описывать назначение функции,
# ее параметры и возвращаемое значение. Часто программисты откладывают написание таких комментариев напоследок,
# а потом и вовсе забывают о них 😂.
#
# На вход программе подается строка текста с именем текстового файла,
# в котором написан код на языке Python. Напишите программу, выводящую на экран имена всех функций для которых
# отсутствует поясняющий комментарий. Будем считать, что любая строка, начинающаяся со слова def и пробела,
# является началом определения функции. Функция содержит комментарий, если первый символ предыдущей строки - #.

filename = input()
with open(filename, 'r', encoding='utf-8') as file_input:
    data = file_input.readlines()

functions = [line for index, line in enumerate(data) if line.startswith('def')
             if index == 0 or not data[index - 1].startswith('#')]

functions = map(lambda x: x.split()[1], functions)
functions = list(map(lambda x: x[:x.rfind('(')], functions))
print(*functions if functions else ("Best Programming Team",), sep='\n')
