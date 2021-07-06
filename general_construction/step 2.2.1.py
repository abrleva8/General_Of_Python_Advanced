# Дан набор точек на координатной плоскости.
# Необходимо подсчитать и вывести количество точек, лежащих в каждой координатной четверти.


def count_of_1(points):
    return sum(point[0] > 0 and point[1] > 0 for point in points)


def count_of_2(points):
    return sum(point[0] < 0 and point[1] > 0 for point in points)


def count_of_3(points):
    return sum(point[0] < 0 and point[1] < 0 for point in points)


def count_of_4(points):
    return sum(point[0] > 0 and point[1] < 0 for point in points)


n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
print(f'Первая четверть: {count_of_1(points)}', f'Вторая четверть: {count_of_2(points)}',
      f'Третья четверть: {count_of_3(points)}', f'Четвертая четверть: {count_of_4(points)}', sep='\n')
