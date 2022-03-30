# Напишите программу, которая с помощью модуля random генерирует nn паролей длиной mm символов,
# состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:
#
# «l» (L маленькое);
# «I» (i большое);
# «1» (цифра);
# «o» и «O» (большая и маленькая буквы);
# «0» (цифра).

import random
import string


def get_string(to_delete):
    _string = string.ascii_letters + string.digits
    for ch in to_delete:
        _string = _string.replace(ch, '')
    return _string


def generate_password(length):
    to_delete = 'lI1oO0'
    _string = get_string(to_delete)
    return ''.join([random.choice(_string) for _ in range(length)])


def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))


n, m = int(input()), int(input())
generate_passwords(n, m)
