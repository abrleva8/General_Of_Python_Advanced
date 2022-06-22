# Вам доступен CSV-файл data.csv, содержащий информацию в csv формате. Напишите функцию read_csv для чтения данных из
# этого файла. Она должна возвращать список словарей, интерпретируя первую строку как имена ключей, а каждую
# последующую строку как значения этих ключей.

filename = 'data.csv'

with open(filename, 'r', encoding='utf-8') as f:
    keys = f.readline().rstrip().split(',')
    data = [dict(zip(keys, line.rstrip().split(','))) for line in f.readlines()]

print(data)
