# Даны по 10-балльной шкале оценки по физике трех учеников. Напишите программу, которая выводит множество оценок
# третьего ученика, которые не встречаются ни у первого, ни у второго ученика.

digits = [set(map(int, input().split())) for _ in range(3)]
result = digits[2] - (digits[0] | digits[1])
print(*sorted(result, reverse=True))
