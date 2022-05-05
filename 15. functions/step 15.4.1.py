# Список athletes содержит сведения о спортсменах в виде кортежей: (имя, возраст, рост, вес).
#
# Напишите программу сортировки списка спортсменов по указанному полю:
#
# 1: по имени;
# 2: по возрасту;
# 3: по росту;
# 4: по весу.

def generator_data_by_index(index):
    def data_by_index(tup):
        return tup[index]
    return data_by_index


index = int(input()) - 1

current_data_by_index = generator_data_by_index(index=index)

athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

athletes.sort(key=current_data_by_index)
[print(*athlete) for athlete in athletes]
