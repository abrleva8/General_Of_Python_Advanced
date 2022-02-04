# Даны по 10-балльной шкале оценки по информатике трех учеников. Напишите программу, которая выводит множество оценок,
# которые есть и у первого и у второго учеников, но которых нет у третьего ученика.

digits = [set(input().split()) for _ in range(3)]
result = (digits[0] & digits[1]) - digits[2]
result = [int(num) for num in result]
print(*sorted(result, reverse=True))
