# Китайский гороскоп назначает животным годы в 12-летнем цикле.
# Например, 2012 год будет очередным годом дракона.
# Напишите программу, которая считывает год и отображает название связанного с ним животного.
# Ваша программа должна корректно работать с любым годом, не только теми, что перечислены в таблице.

zodiacs = ['Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц', 'Дракон', 'Змея', 'Лошадь', 'Овца']
print(zodiacs[int(input()) % 12])