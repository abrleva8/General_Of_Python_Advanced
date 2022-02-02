# На вход программе подается строка текста, содержащая числа. Для каждого числа выведите слово YES (в отдельной строке),
# если это число ранее встречалось в последовательности или NO, если не встречалось.

nums_to_add = input().split()
numbers = set()
for num in nums_to_add:
    num = int(num)
    print('YES' if num in numbers else 'NO')
    numbers.add(num)
