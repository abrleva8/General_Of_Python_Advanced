# Необходимо написать программу, реализующую алгоритм написания https://www.youtube.com/watch?v=sAuMERnj-FU песни.
# Алгоритм выводит в конце предложения следующую в алфавитном порядке букву,
# если она встречается в строке текста, а очередную строку отображает уже без этой буквы.

alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
        'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

string = input() + ' запретил букву'

for ch in alph:
    if ch in string:
        string = string.replace('  ', ' ')
        print(string, ch)
        string = string.replace(ch, '').strip()
