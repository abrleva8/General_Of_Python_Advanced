# Дана строка текста на русском языке, состоящая из слов и символов пробела.
# Словом считается последовательность букв, слова разделены одним пробелом или несколькими.
#
# Напишите программу, определяющую для каждого слова порядковый номер его вхождения в текст именно в этой форме,
# с учетом регистра. Для первого вхождения слова программа выведет 11, для второго вхождения того же слова — 22 и т. д.

def print_quantity_dict(words: list):
    my_dict = {}
    for word in words:
        my_dict[word] = my_dict.get(word, 0) + 1
        print(my_dict[word], end=' ')
    return my_dict


words = input().split()
print_quantity_dict(words)
