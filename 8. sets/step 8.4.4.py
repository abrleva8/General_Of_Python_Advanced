# На вход программе подаются две строки, состоящие из цифр.
# Необходимо определить, верно ли, что для записи этих строк были использованы одинаковые наборы цифр?

print('YES' if set(input()) == set(input()) else 'NO')