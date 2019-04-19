# урок 04, задание 2 (уровень hard)

# Найдите наибольшее произведение пяти последовательных цифр 
# в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа 
# последовательных 5-ти цифр.

__author__ = 'Караваев Илья Викторович'

import random


def multiplication(S):  # расчет произведения цифр в последовательности S
    M = 1               # начальное значение
    for s in S:
        M *= int(s)
    return M


def maxMultiplSearch(S, n=5):
    found = []      # для хранения всех найденных последовательностей
    i_start = 0     # начальная позиция последовательности    
    while S:
        group = S[:n]       # очередные n цифр        
        # сохраняем произведение и начальную позицию:
        found.append((multiplication(group), i_start))       
        if len(S) <= n: # подсчет произведений цифр заканчивается за n цифр
            break       # до конца последовательности S
        S = S[1:]       # сдвигаем строку на 1 цифру
        i_start +=1     # увеличиваем счетчик позиции
    max_found = (0, 0)
    for item in found:  # ищем максимальное произведение
        if item[0] > max_found[0]:
            max_found = item
    return ('Наибольшее произведение ' + str(n) + 
            ' последовательных цифр равно ' + str(max_found[0]) + 
            ';\nиндекс смещения первой цифры группы: ' + 
            str(max_found[1]) + '\n')



length = 1000   # длина цифровой последовательности
data = ''

for i in range(length):
    data += str(random.randint(0, 9))
print('Исходная ' + str(length) + '-значная последовательность:' 
        + 2 * '\n' + data + '\n')

print(maxMultiplSearch(data))
print(maxMultiplSearch(data, 3))
print(maxMultiplSearch(data, 7))
