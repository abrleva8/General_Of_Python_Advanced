# Вам доступен текстовый файл prices.txt с информацией о заказе из интернет магазина.
# В нем каждая строка с помощью символа табуляции (\t) разделена на три колонки:
#
# наименование товара;
# количество товара (целое число);
# цена (в рублях) товара за 1 шт (целое число).
# Напишите программу, выводящую на экран общую стоимость заказа.

def sum_of_line(line):
    data = line.split('\t')
    return int(data[1]) * int(data[2])


filename = 'prices.txt'
file = open(filename, 'r', encoding='utf-8')
print(sum(map(sum_of_line, file)))
file.close()
