# На вход программе подаются две строки текста, содержащие числа. Напишите программу,
# которая выводит все числа в порядке возрастания, которые есть в первой строке, но отсутствуют во второй.

first = [int(num) for num in input().split()]
second = [int(num) for num in input().split()]
dif = set(first) - set(second)
print(*sorted(dif))
