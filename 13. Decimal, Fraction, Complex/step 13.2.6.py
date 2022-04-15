# На вход программе подается натуральное число n. Напишите программу, которая выводит в порядке возрастания все
# несократимые дроби, заключённые между 0 и 1, знаменатель которых не превосходит n.

from fractions import Fraction


def get_fractions(n: int):
    return {Fraction(j, i) for i in range(1, n + 1) for j in range(1, i)}


n = int(input())
print(*sorted(get_fractions(n)), sep='\n')
