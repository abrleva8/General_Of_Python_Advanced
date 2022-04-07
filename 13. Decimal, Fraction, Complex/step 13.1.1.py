# На вход программе подается Decimal число dd. Напишите программу, которая вычисляет значение выражения:
# e^d + ln(d) + lg(d) +sqrt(d)

from decimal import Decimal

num = Decimal(input())
num = num.exp() + num.ln() + num.log10() + num.sqrt()
print(num)
