# Напишите программу для определения общего количества различных слов в строке текста.

def preprocessing(string):
    string = string.lower()
    to_delete = '.,;:-?!'
    for sym in to_delete:
        string = string.replace(sym, '')

    return string.split()


def count_of_words(sentence):
    words = set()

    for word in sentence:
        words.add(word)
    return len(words)


sentence = input()
sentence = preprocessing(sentence)
res = count_of_words(sentence)
print(res)
