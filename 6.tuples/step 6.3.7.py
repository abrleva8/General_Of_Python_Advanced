# Напишите программу, которая считывает натуральное число n и выводит первые n чисел последовательности Трибоначчи.

def print_tribonacci(n):
    f1, f2, f3 = 1, 1, 1
    for _ in range(n):
        print(f1, end=' ')
        f1, f2, f3 = f2, f3, f1 + f2 + f3


n = int(input())
print_tribonacci(n)
