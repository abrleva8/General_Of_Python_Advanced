# На вход программе подается натуральное число n.Напишите программу, которая вычисляет и выводит рациональное число,
# равное значению выражения 1/1! + 1/2! + 1/3! + ... + 1/n!

from fractions import Fraction
from math import factorial


def sum_of_reverse_factorials(n):
    return sum(Fraction(1, factorial(i)) for i in range(1, n + 1))


n = int(input())
print(sum_of_reverse_factorials(n))
