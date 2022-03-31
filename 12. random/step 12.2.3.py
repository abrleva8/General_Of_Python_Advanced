# Напишите программу, которая с помощью модуля random генерирует nn паролей длиной mm символов,
# состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:
#
# «l» (L маленькое);
# «I» (i большое);
# «1» (цифра);
# «o» и «O» (большая и маленькая буквы);
# «0» (цифра).

# Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра
# и как минимум по одной букве в верхнем и нижнем регистре.

import random
import string


def get_string(to_delete):
    _string = string.ascii_letters + string.digits
    for ch in to_delete:
        _string = _string.replace(ch, '')
    return _string


def generate_password(length):
    to_delete = 'lI1oO0'
    _digits = '2345678'
    uppercase_letters = 'abcdefghijkmnpqrstuvwxyz'
    capital_letters = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
    _string = get_string(to_delete)
    password = [random.choice(_string) for _ in range(length - 3)]
    password.append(random.choice(_digits))
    password.append(random.choice(uppercase_letters))
    password.append(random.choice(capital_letters))
    random.shuffle(password)
    return ''.join(password)


def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))


n, m = int(input()), int(input())
generate_passwords(n, m)
