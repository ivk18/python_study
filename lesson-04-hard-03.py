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

# отобразить положение ферзей на "доске"
def showBoard():
    coord = coordGen()
    #print(str(coord) + str('\n'*2))    # отобразить координаты для проверки
    board = []
    [board.append([]) for i in range(8)]
    for i in range(8):
        for j in range(8):
            if (i, j) in coord:
                board[i].append("X")
            else:
                board[i].append("O")
            print(board[i][j], end="  ")
        print('\n')

showBoard()
