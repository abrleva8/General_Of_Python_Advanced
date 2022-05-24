# Хороший пароль по условиям этой задачи состоит как минимум из 7 символов, содержит хотя бы одну цифру, заглавную и
# строчную букву. Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль.
import string


def is_has_string(string, password):
    return any(map(lambda x: x in string, password))


password = input()
is_has_lower = is_has_string(string.ascii_lowercase, password)
is_has_upper = is_has_string(string.ascii_uppercase, password)
is_has_digit = is_has_string(string.digits, password)

is_good_password = all[is_has_lower, is_has_upper, is_has_digit, len(password) >= 7]
print("YES" if is_good_password else "NO")
