# Ученики 10 класса онлайн-школы BEEGEEK получили задание прочесть на летних каникулах три книги:
#
# "Что такое математика?";
# "Математическая составляющая";
# "100 гениальных идей по математике".
# Оказалось, что n учеников прочитали первую книгу, m учеников — вторую, k учеников — третью. Также известно, что x
# учеников прочли первую или вторую, или обе эти книги, y учеников — вторую или третью, или обе, z учеников — первую и
# третью, или хотя бы одну из этих двух книг. Полностью выполнили задание только t учеников. Всего в 10 классе учится a
# учеников. Напишите программу, которая выводит сколько учеников:
# прочитали только одну книгу;
# прочитали две книги;
# не прочитали ни одной из рекомендованных книг.

n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]
n_m_k, x_y_z = m + n + k, x + y + z
print(2 * x_y_z + 3 * t - 3 * n_m_k)
print(2 * n_m_k - x_y_z - 3 * t)
print(a + n_m_k - x_y_z - t)
