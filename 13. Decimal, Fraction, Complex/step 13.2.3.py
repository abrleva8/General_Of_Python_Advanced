# На вход программе подается натуральное число n.Напишите программу, которая вычисляет и выводит рациональное число,
# равное значению выражения 1/1^2 + 1/2^2 + 1/3^2 + ... + 1/n^2

from fractions import Fraction


def sum_of_reverse_square(n):
    return sum(Fraction(1, i**2) for i in range(1, n + 1))


n = int(input())
print(sum_of_reverse_square(n))
