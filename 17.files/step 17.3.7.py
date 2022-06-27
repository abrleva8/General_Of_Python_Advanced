# Вам доступен текстовый файл logfile.txt с информацией о времени входа пользователя в систему и выхода из нее.
# Каждая строка файла содержит три значения, разделенные запятыми и символом пробела: имя пользователя,
# время входа, время выхода, где время указано в 24-часовом формате.
#
# Напишите программу, которая создает файл output.txt и выводит в него имена всех пользователей
# (не меняя порядка следования), которые были в сети не менее часа.\

def is_more_an_hour(start_date, finish_date):
    start_hours, start_minutes = map(int, start_date.split(':'))
    finish_hours, finish_minutes = map(int, finish_date.split(':'))
    if finish_hours == start_hours:
        return False
    if start_hours == 1 and start_minutes > finish_minutes:
        return False
    return True


filename_input = 'logfile.txt'
filename_output = 'output.txt'

with open(filename_input, 'r', encoding='utf-8') as file_input:
    data = map(lambda x: x.rstrip().split(','), file_input.readlines())

filtered_data = filter(lambda el: is_more_an_hour(el[1], el[2]), data)

with open(filename_output, 'w', encoding='utf-8') as file_output:
    print(*map(lambda el: el[0], filtered_data), file=file_output, sep='\n')
