def get_top_of_the_parabola(a, b, c):
    x = - b / (2 * a)
    y = (4 * a * c - b * b) / (4 * a)
    return x, y


a, b, c = int(input()), int(input()), int(input())
top = get_top_of_the_parabola(a, b, c)
print(top)
