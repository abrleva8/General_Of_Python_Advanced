# На вход программе подаются два числа. Напишите программу, определяющую, есть ли в данных числах одинаковые цифры.

first_digits, second_digits = map(set, [input(), input()])
print('YES' if first_digits & second_digits else 'NO')
