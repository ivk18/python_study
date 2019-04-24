# урок 05, задание 3 (уровень easy)

# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

__author__ = 'Караваев Илья Викторович'

import os
import shutil

curr_file_ext = os.path.basename(__file__)  # имя запущенного скрипта
curr_file = os.path.splitext(curr_file_ext)[0]  # имя без расширения файла
# имя файла - копии:
new_file = str(curr_file) + '_copy' + os.path.splitext(curr_file_ext)[-1]

shutil.copyfile(curr_file_ext, new_file)
