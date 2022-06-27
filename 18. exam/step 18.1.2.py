# Вам доступен текстовый файл ledger.txt с данными о продажах фирмы за месяц.
# На каждой строке файла указано, сколько клиент заплатил за товар, в долларах (целое число):

filename = 'ledger.txt'
with open(filename, 'r', encoding='utf-8') as file:
    print('$' + str(sum(map(lambda x: int(x[1:]), file.read().split('\n')))))
