# урок 01, задание 1 (уровень easy)

# Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

__author__ = 'Караваев Илья Викторович'

x = z = input('Введите значение 1й переменной: ')
y = input('Введите значение 2й переменной: ')
x = y
y = z
print('\n\nНовая 1я переменная: ' + str(x))
print('Новая 2я переменная: ' + str(y) + '\n')
