# Тимур записал телефоны всех своих друзей, чтобы автоматизировать поиск нужного номера.
# У каждого из друзей Тимура может быть один или более телефонных номеров. Напишите программу,
# которая поможет Тимуру находить все номера определённого друга.

n = int(input())
my_dict = {}
for _ in range(n):
    number, name = input().lower().split()
    value = my_dict.setdefault(name, []).append(number)

n = int(input())
for _ in range(n):
    name = input().lower()
    print(*my_dict.get(name, ['абонент не найден']))
