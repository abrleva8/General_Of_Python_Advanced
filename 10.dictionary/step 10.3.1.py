# На вход программе подается строка текста.
# Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

extra_symbols = '.,!?:;-'
string = input()

for symbol in extra_symbols:
    string = string.replace(symbol, '')

words = string.lower().split()
result = {}
for word in words:
    result.setdefault(word, 0)
    result[word] += 1

max_value = min(result.values())
for key in sorted(result.keys()):
    if result[key] == max_value:
        print(key)
        break
