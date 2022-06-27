# На вход программе подается строка текста с именем текстового файла. Напишите программу,
# выводящую на экран содержимое этого файла, но с заменой всех запрещенных слов звездочками *
# (количество звездочек равно количеству букв в слове).
#
# Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt.
# Гарантируется, что все слова в этом файле записаны в нижнем регистре.

filename = 'forbidden_words.txt'
with open(filename, 'r', encoding='utf-8') as file:
    forbidden_words = file.read().split()

filename = input()
with open(filename, 'r', encoding='utf-8') as file:
    data = file.read()

data_copy = str(data).lower()
for forbidden_word in forbidden_words:
    data_copy = data_copy.replace(forbidden_word, len(forbidden_word) * '*')

print(''.join([el if el == '*' else data[index] for index, el in enumerate(data_copy)]))
