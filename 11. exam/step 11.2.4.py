# В файловую систему компьютера, на котором развернута наша ❤️ платформа Stepik, проник опасный вирус и сломал
# контроль прав доступа к файлам. Говорят, вирус написал один из студентов курса Python для начинающих.
#
# Для каждого файла известно, с какими действиями можно к нему обращаться:
#
# запись W (write, доступ на запись в файл);
# чтение R (read, доступ на чтение из файла);
# запуск X (execute, запуск на исполнение файла).
# Напишите программу для восстановления контроля прав доступа к файлам.
# Ваша программа для каждого запроса должна будет возвращать OK если выполняется допустимая операция,
# и Access denied, если операция недопустима.

def get_dict(n: int):
    my_dict = {}
    for _ in range(n):
        key, value = input().split(' ', 1)
        my_dict[key] = value
    return my_dict


abbreviation = {'write': 'W', 'read': 'R', 'execute': 'X'}

n = int(input())
file_dict = get_dict(n)
print(file_dict)
m = int(input())
for _ in range(m):
    command, file = input().split()
    print('OK' if abbreviation[command] in file_dict[file] else 'Access denied')
