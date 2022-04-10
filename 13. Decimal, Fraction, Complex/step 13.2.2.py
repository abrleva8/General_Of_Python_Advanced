# Даны две дроби в формате a/b. Напишите программу, которая вычисляет и выводит их сумму, разность, произведение и
# частное.

from fractions import Fraction

number_str_1, number_str_2 = input(), input()

print(f'{number_str_1} + {number_str_2} = {Fraction(number_str_1) + Fraction(number_str_2)}')
print(f'{number_str_1} - {number_str_2} = {Fraction(number_str_1) - Fraction(number_str_2)}')
print(f'{number_str_1} * {number_str_2} = {Fraction(number_str_1) * Fraction(number_str_2)}')
print(f'{number_str_1} / {number_str_2} = {Fraction(number_str_1) / Fraction(number_str_2)}')
