# Дана строка из разделенных пробелами слов в разных регистрах. Напишите программу, которая отсортирует слова
# независимо от регистра, а затем выведет их. Отсортированные слова должны выводиться на печать в исходном регистре,
# в каком переданы программе на вход.

print(*sorted(input().split(), key=lambda word: word.lower()))
