# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников.
# Теперь он использует их в качестве серверов "Пегого дудочника".
# Помогите владельцу фирмы отыскать все зараженные холодильники.

# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует
# слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв),
# то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы

def some_func(string):
    if string.count('n') < 2:
        return False
    arr = list('anton')
    index = 0
    for ch in arr:
        if string.find(ch, index) > -1:
            index = string.find(ch, index)
        else:
            return False
    return True


n = int(input())
# print(i + 1 if some_func() else '' for i in range(n))
for i in range(n):
    if some_func(input()):
        print(i + 1, end=' ')
