# урок 05, задание 2 (уровень easy)

# Напишите скрипт, отображающий папки текущей директории.

__author__ = 'Караваев Илья Викторович'

import os
curr_dir = os.getcwd()  # текущая папка

print('Перечень папок текущей директории:' + str('\n'))
for item in os.listdir(): 
    if os.path.isdir(item):
        print(item)
