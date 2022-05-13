# На вход программе подаются три строки текста с вещественными числами, значениями абсцисс (x), ординат (y) и аппликат
# (z) точек трехмерного пространства. Напишите программу для проверки расположения всех точек с введенными координатами
# внутри либо на поверхности шара с центром в начале координат и радиусом R = 2.

abscissas = map(float, input().split())
ordinates = map(float, input().split())
applicates = map(float, input().split())
r = 2

print(all(map(lambda point: point[0]**2 + point[1]**2 + point[2]**2 <= r**2, zip(abscissas, ordinates, applicates))))
