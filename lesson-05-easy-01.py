# урок 05, задание 1 (уровень easy)

# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

__author__ = 'Караваев Илья Викторович'

import os
curr_dir = os.getcwd()  # текущая папка

for i in range(1, 10):
    dir_name = 'dir_{}'.format(i)   # имя новой папки
    dir_path = os.path.join(curr_dir, dir_name) # путь новой папки
    try:
        os.mkdir(dir_path) # создаем папку
    except FileExistsError:
        print('Директория {} уже существует'.format(dir_name))

print('Содержимое текущей папки:' + str('\n'))
for item in os.listdir(): print(item)
print()

del_flag = input('Нажмите "1", чтобы удалить папки "dir_*": ')

if del_flag == '1':
    for i in range(1, 10):
        dir_name = 'dir_{}'.format(i)   # имя удаляемой папки
        try:
            os.rmdir(dir_name) # удаляем папку
        except FileNotFoundError:
            print('Директория {} не найдена'.format(dir_name))

    print(str('\n') + 'Содержимое текущей папки:' + str('\n'))
    for item in os.listdir(): print(item)
