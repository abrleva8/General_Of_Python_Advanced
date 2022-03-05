# На вход программе подаются два предложения. Напишите программу, которая определяет, являются они анаграммами или нет.
# Ваша программа должна игнорировать регистр символов, знаки препинания и пробелы.

def get_word_dict(string: str) -> dict:
    my_dict = {}
    for char in string:
        if char.isalpha():
            my_dict[char] = my_dict.get(char, 0) + 1
    return my_dict


s1, s2 = input().lower(), input().lower()
s1_dict, s2_dict = get_word_dict(s1), get_word_dict(s2)
print('YES' if s1_dict == s2_dict else 'NO')
