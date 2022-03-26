# Напишите программу, которая случайным образом назначает каждому ученику его тайного друга,
# который будет вместе с ним решать задачи по программированию.
import random


def print_dict(my_dict):
    for key in my_dict.keys():
        print(f'{key} - {my_dict[key]}')


n = int(input())
names = [input() for _ in range(n)]
names_santa = dict.fromkeys(names)
print(names_santa)

random.shuffle(names)
for index, name in enumerate(names):
    names_santa[name] = names[(index + 1) % len(names)]

print_dict(my_dict=names_santa)
