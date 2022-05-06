# На вход программе подается строка натуральных чисел. Из элементов строки формируется список чисел.
#
# Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр. При этом, если у двух чисел одинаковая
# сумма цифр, их следует вывести в порядке неубывания.

def sum_of_digit_and_number(number: int) -> int:
    return sum([int(digit) for digit in str(number)]), number


li = list(map(int, input().split()))
li.sort(key=sum_of_digit_and_number)
print(*li)
