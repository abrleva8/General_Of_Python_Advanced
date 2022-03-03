# На вход программе подаются два слова. Напишите программу, которая определяет, являются ли они анаграммами.

def get_word_dict(string: str) -> dict:
    my_dict = {}
    for char in string:
        my_dict[char] = my_dict.get(char, 0) + 1
    return my_dict


s1, s2 = input(), input()
s1_dict, s2_dict = get_word_dict(s1), get_word_dict(s2)
print('YES' if s1_dict == s2_dict else 'NO')
