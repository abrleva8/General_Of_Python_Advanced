# На вход программе подается строка текста, содержащая символы.
# Напишите программу, которая упаковывает последовательности одинаковых символов заданной строки в подсписки.

a = input().split()
res = [[a[0]]]
n = len(a)
for i in range(1, n):
    if a[i] == a[i - 1]:
        res[-1].append(a[i])
    else:
        res.append([a[i]])
print(res)
