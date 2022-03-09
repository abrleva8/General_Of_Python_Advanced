# Напишите программу для подсчета количества единиц каждого вида товара из приобретенных
# каждым покупателем интернет-магазина.

def get_dict(n: int):
    my_dict = {}
    for _ in range(n):
        key, value = input().split(' ', 1)
        my_dict.setdefault(key, []).append(value)
    return my_dict


def get_sum_dict(set_: set):
    sum_dict = {}
    for el in set_:
        key, value = el.split(' ', 1)
        sum_dict[key] = sum_dict.setdefault(key, 0) + int(value)
    return sum_dict
    

n = int(input())
purchases = get_dict(n)
purchases = dict(sorted(purchases.items()))

for name, purchase in purchases.items():
    print(f'{name}:')
    sum_dict = get_sum_dict(purchase)
    sum_dict = dict(sorted(sum_dict.items()))
    for key, value in sum_dict.items():
        print(f'{key} {value}')
