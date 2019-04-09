# урок 02, задание 2 (уровень easy)

# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

__author__ = 'Караваев Илья Викторович'

list1 = ['пароль', 'файл', 2348, 'code', 'type', 'qwerty', 'message']
list2 = ['type', 'qwerty', 'стиль', 234, 'mes']

print('Список 1:\n' + str(list1))
print('\nСписок 2:\n' + str(list2))

i = 0
while i < len(list1):
    if list1[i] in list2:
        list1.remove(list1[i])
        continue
    else: i += 1

print('\nСписок 1 без элементов списка 2:\n' + str(list1) + '\n')
