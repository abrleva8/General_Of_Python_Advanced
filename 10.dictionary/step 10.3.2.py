# На вход программе подается строка, содержащая строки-идентификаторы. Напишите программу,
# которая исправляет их так, чтобы в результирующей строке не было дубликатов. Для этого необходимо прибавлять к
# повторяющимся идентификаторам постфикс _n, где n – количество раз, сколько такой идентификатор уже встречался.

strings = input().split()
words_dict = {}
for string in strings:
    words_dict.setdefault(string, 0)
    print(f'{string}', end='')
    print(f'_{words_dict[string]}' if words_dict[string] else '', end=' ')
    words_dict[string] += 1
