# Вам доступен текстовый файл words.txt со словами, разделенными пробелом.
# Напишите программу, которая находит и выводит самые длинные слова этого файла, не меняя порядка их следования.

filename = 'words.txt'
with open(filename, 'r', encoding='utf-8') as file:
    data = file.read().split()

max_len = len(max(data, key=len))
print(*filter(lambda x: len(x) == max_len, data), sep='\n')

