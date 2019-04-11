# урок 03, задание 1 (уровень normal)

# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

__author__ = 'Караваев Илья Викторович'


import math

def fibonacci(n, m):
    F = []
    phi = (1 + math.sqrt(5)) / 2
    for x in range(n, m + 1):
        f = int(round((phi ** x) / math.sqrt(5), 0))
        F.append(f)    
    return F
    
print(fibonacci(4, 13))
