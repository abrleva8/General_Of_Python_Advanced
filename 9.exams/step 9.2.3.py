# Тимур и Руслан играют в игру города. Они очень любят эту игру и знают много городов, особенно Тимур,
# однако к концу игры ввиду своего возраста забывают, какие города уже называли.
#
# Напишите программу, считывающую информацию об игре и сообщающую ребятам, что очередной город назван повторно.

n = int(input())
cities = {input() for _ in range(n + 1)}
print('OK' if len(cities) == n + 1 else 'REPEAT')
