# На вход программе подаются две строки текста, содержащие числа. Напишите программу, которая выводит
# все числа в порядке возрастания, которые есть как в первой строке, так и во второй.

first = [int(num) for num in input().split()]
second = [int(num) for num in input().split()]
intersection = set(first) & set(second)
print(*sorted(intersection))
