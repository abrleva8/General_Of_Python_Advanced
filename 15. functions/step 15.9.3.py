# На вход программе подаются два натуральных числа aa и bb. Напишите программу с использованием встроенной функции
# all() для обнаружения всех целых чисел в диапазоне [a;b],
# которые делятся на каждую содержащуюся в них цифру без остатка.

def is_needed_number(x: int) -> bool:
    return all(symbol != '0' and x % int(symbol) == 0 for symbol in str(x))


a, b = int(input()), int(input())
print(*filter(is_needed_number, range(a, b + 1)))
