# Даны по 10-балльной шкале оценки по биологии трех учеников. Напишите программу, которая выводит множество оценок,
# не встречающихся ни у одного из трех учеников.

total_digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
digits = [set(map(int, input().split())) for _ in range(3)]
result = total_digits - (digits[0] | digits[1] | digits[2])
print(*sorted(result))
