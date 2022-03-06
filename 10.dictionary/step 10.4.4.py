# Вам дан словарь, состоящий из пар слов-синонимов. Повторяющихся слов в словаре нет. Напишите программу,
# которая для одного данного слова определяет его синоним.

n = int(input())
my_dict = {}
for _ in range(n):
    word_1, word_2 = input().split()
    my_dict[word_1] = word_2
    my_dict[word_2] = word_1

word = input()
print(my_dict[word])
