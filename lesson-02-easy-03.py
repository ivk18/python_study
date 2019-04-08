# урок 02, задание 3 (уровень easy)

__author__ = 'Караваев Илья Викторович'

list1 = [23, 2, 12, 95, 76, 69, 64, 37, 49, 56]
list2 = []

for i in range(len(list1)):
    if list1[i] % 2 == 0:
        list2.append(list1[i] / 4)
    else:
        list2.append(list1[i] * 2)
        
print('Исходный список:\n' + str(list1))
print('\nНовый список:\n' + str(list2) + '\n')
