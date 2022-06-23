# Однажды Жака Фреско спросили:
# "Если ты такой умный, почему не богатый?"
# Жак не стал отвечать на столь провокационный вопрос, вместо этого он задал загадку спрашивающему:
# "Были разноцветные козлы. Сколько?"
# "Сколько чего?"
# "Сколько из них составляет более 7% от общего количества козлов?"
# Вам доступен текстовый файл goats.txt в первой строке которого написано слово COLOURS,
# далее идет список всех возможных цветов козлов. Затем идет строка со словом GOATS,
# и далее непосредственно перечисление козлов разных цветов.
# Перечень козлов включает только строки из первого списка.
#
# Напишите программу создания файла answer.txt и вывода в него списка козлов,
# которые удовлетворяют условию загадки от Жака Фреско.
filename_input = 'goats.txt'
filename_output = 'answer.txt'

with open(filename_input, 'r', encoding='utf-8') as f:
    f.readline()
    colors = []
    line = f.readline()
    while line.rstrip() != 'GOATS':
        colors.append(line.split()[0])
        line = f.readline()
    data = list(map(lambda x: x.split()[0], f.readlines()))

colors = list(filter(lambda col: data.count(col)/len(data) > 0.07, colors))

with open(filename_output, 'w', encoding='utf-8') as f:
    for el in colors:
        print(f'{el} goat', file=f, end='')
