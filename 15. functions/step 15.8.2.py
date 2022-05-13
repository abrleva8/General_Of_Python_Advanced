# Многочленом степени n называется выражение вида a_n*x ^ n + a_{n - 1}* x ^ {n - 1} +...+ a_2x ^ 2 + a_1x + a_0,
# где a_n, a_{n - 1}... a_2, a_1, a_0  — коэффициенты многочлена. На вход программе на строке подаются коэффициенты
# многочлена, разделенные символом пробела и целое число x на второй строке.
# Напишите программу, которая вычисляет значение указанного многочлена при заданном значении x.


from functools import reduce


def evaluate(coefficients, x):
    list_x = [x**i for i in range(len(coefficients))]
    monomials = map(lambda a, b: a * b, coefficients[::-1], list_x)
    return reduce(lambda a, b: a + b, monomials, 0)


coefficients = list(map(int, input().split()))
x = int(input())
print(evaluate(coefficients, x))
