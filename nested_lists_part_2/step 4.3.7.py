# Подсписок — часть другого списка. Подсписок может содержать один элемент, несколько, и даже ни одного.
# Например, [1], [2], [3] и [4] — подсписки списка [1, 2, 3, 4]. Список [2, 3] — подсписок списка [1, 2, 3, 4],
# но список [2, 4] не подсписок списка [1, 2, 3, 4], так как элементы 2 и 4 во втором списке не смежные.
# Пустой список — подсписок любого списка. Сам список — подсписок самого себя,
# то есть список [1, 2, 3, 4] подсписок списка [1, 2, 3, 4].
#
# На вход программе подается строка текста, содержащая символы. Из данной строки формируется список.
# Напишите программу, которая выводит список, содержащий все возможные подсписки списка, включая пустой список.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая символы, отделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести указанный список, содержащий все возможные подсписки,
# включая пустой список в соответствии с примерами.
#
# Примечание. Порядок списков одинаковой длины должен соответствовать порядку их вхождения в основной список.

def chunked(li, num):
    if num == 0:
        return [[]]
    return [li[i: i + num] for i in range(0, len(li) - num + 1)]


def get_sub_lists(li):
    res = []
    for size in range(len(li) + 1):
        res.extend(chunked(li, size))
    return res


some_list = input().split()
result = get_sub_lists(some_list)
print(result)
