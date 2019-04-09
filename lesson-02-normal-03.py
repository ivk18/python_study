# урок 02, задание 3 (уровень normal)

# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

__author__ = 'Караваев Илья Викторович'

import random
random_list = []

while True:
    try:
        n = int(input('Введите количество элементов списка: '))
        if n <= 0: 
            print('\n\tВведите целое число больше нуля!\n')
            continue
    except:
        print('\n\tВведите целое число больше нуля!\n')
    else:
        break

for i in range(n):
    random_list.append(random.randint(-100, 100))
    
print('\n' + str(random_list) + '\n')
