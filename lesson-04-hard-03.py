# урок 04, задание 3 (уровень hard)

# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

__author__ = 'Караваев Илья Викторович'


# генерируем случайные координаты 8 ферзей
def coordGen():
    from random import randint
    coord = []
    quantity = 8
    while quantity:
        x = (randint(0, 7), randint(0, 7))
        if x in coord:
            continue
        else:
            coord.append(x)
            quantity -= 1       
    return coord

# отображаем положение ферзей на "доске"
def showBoard(items):
    # print(str(items) + str('\n'*2))    # отобразить координаты для проверки
    board = []
    [board.append([]) for i in range(8)]
    for i in range(8):
        for j in range(8):
            if (i, j) in items:
                board[i].append("X")
            else:
                board[i].append("O")
            print(board[i][j], end="  ")
        print('\n')

# проверка угрозы ферзей друг другу
def checkAttack():
    global flag
    coord = coordGen()
    showBoard(coord)
    start_item = coord[0]
    coord = coord[1:]
    result = []
    while coord:
        for item in coord:
            # если ферзи на одной горизонтали, вертикали или диагонали,
            # то они угрожают друг другу
            if (start_item[0] == item[0] or start_item[1] == item[1] or
                abs(start_item[0] - item[0]) == abs(start_item[1] - item[1])):              
                result.append(start_item)
                result.append(item)
        start_item = coord[0]
        coord = coord[1:]
    result = set(result)
    result = list(result)
    if not result: flag = False
    return result

flag = True   
quantity = 0         
import os
            
while flag:
    os.system('cls')
    print('Первоначальная расстановка ферзей: ' + str('\n'))            
    res = checkAttack()
    print(str('\n') + 'Ферзи под "боем": ' + str('\n') + str(res) + str('\n'*2))
    print('Расстановка ферзей под "боем": ' + str('\n')) 
    showBoard(res)
    quantity += 1
    print((str('\n'*2) + 'Проверено расстановок: ' + str(quantity)))
