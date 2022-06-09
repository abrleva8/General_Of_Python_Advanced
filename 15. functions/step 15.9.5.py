# Учитель Тимур проверял контрольные работы по математике в нескольких классах онлайн-школы BEEGEEK и решил убедиться,
# что в каждом классе есть хотя бы один отличник – ученик с оценкой 5 по контрольной работе.
# Напишите программу с использованием встроенных функций all(), any() для помощи Тимуру в проверке.

n = int(input())
is_any = []
for _ in range(n):
    grades = map(int, [input().split()[1] for i in range(int(input()))])
    is_any.append(any(el == 5 for el in grades))

print("YES" if all(is_any) else "NO")
