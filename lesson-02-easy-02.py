# урок 02, задание 2 (уровень easy)

# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

__author__ = 'Караваев Илья Викторович'

list1 = ['пароль', 'файл', 2348, 'code', 'type', 'qwerty', 'message']
list2 = ['type', 'qwerty', 'стиль', 234, 'mes']
list3 = []

print('Список 1:\n' + str(list1))
print('\nСписок 2:\n' + str(list2))

for l1 in list1:
    if l1 not in list2: list3.append(l1)

print('\nСписок 1 без элементов списка 2:\n' + str(list3) + '\n')
