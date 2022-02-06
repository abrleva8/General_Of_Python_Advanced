# Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба этих предмета.
# У руководителя школы есть списки изучающих каждый предмет.
#
# Напишите программу, позволяющую руководителю выяснить, сколько учеников изучает только один предмет.

m, n = int(input()), int(input())
maths = {input() for _ in range(m)}
informatics = {input() for _ in range(n)}
only_one = maths ^ informatics
print(len(only_one) if only_one else 'NO')
