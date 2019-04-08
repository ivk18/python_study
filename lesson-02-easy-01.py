# урок 02, задание 1 (уровень easy)

__author__ = 'Караваев Илья Викторович'

fruits = ["яблоко", "банан", "киви", "арбуз", "виноград", "лимон", 
"айва", "апельсин"]
length = 0      # переменная для подсчета максимальной длины элемента списка

for fruit in fruits:
    # поиск самого длинного элемента списка:
    if len(fruit.strip()) > length: length = len(fruit.strip())     

for i in range(len(fruits)):
    print("{0}. {1:>{2}}".format(i + 1, fruits[i].strip(), length))
