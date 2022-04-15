# Дима учится в седьмом классе и сейчас они проходят обыкновенные дроби с натуральными числителем и знаменателем.
# Вчера на уроке математики Дима узнал, что дробь называется правильной, если ее числитель меньше знаменателя, и
# несократимой, если нет равной ей дроби с меньшими натуральными числителем и знаменателем.
# Дима очень любит математику, поэтому дома он долго экспериментировал, придумывая и решая разные задачки с
# правильными несократимыми дробями. Одну из этих задач Дима предлагает решить вам с помощью компьютера.
#
# На вход программе подается натуральное число nn. Напишите программу, которая находит наибольшую правильную
# несократимую дробь с суммой числителя и знаменателя равной n.

from fractions import Fraction


def get_answer(n: int):
    half = n // 2
    if n % 2 == 1:
        return Fraction(half, half + 1)
    elif n % 4 == 0:
        return Fraction(half - 1, half + 1)
    return Fraction(half - 2, half + 2)


n = int(input())
print(get_answer(n))