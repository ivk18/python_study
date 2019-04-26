# Игра "крестики - нолики".

from random import randint
from os import system


def moveGen(game_field):
    """
    Генерация случайных координат хода компьютера.
    Функция принимает состояние игрового поля (game_field).???????
    """
    global turn
    while True:
        coord = randint(0, 2), randint(0, 2)
        if coord not in game_field and turn == 1:
            game_field.append(coord)
            quantity -= 1
            turn = 0
        else:
            continue
    return coord       # возвращаем координаты хода компьютера


def showMove(move, game_field):
    """
    Отображение текущего хода на игровом поле.
    Функция принимает кортеж с координатами хода (move)
    и текущее состояние игрового поля (game_field).
    """
    os.system('cls')
    board = []
    [board.append([]) for i in range(3)]
    for i in range(3):
        for j in range(3):
            if (i, j) in game_field:
                board[i].append("X")
            else:
                board[i].append("O")
            print(board[i][j], end="  ")
        print('\n')

        
def playerMove():
    """
    Запрос координат хода игрока.
    """
    global turn
    x = int(input('Введите координату Х своего хода: '))
    y = int(input('Введите координату Y своего хода: '))
    move = x, y  # координаты хода игрока (кортеж)
    turn = 1     # флаг перехода хода к компьютеру
    
    


turn = randint(0, 1)    # определение очередности первого хода

# если turn = 1 - первый ход делает компьютер, если turn = 0 - игрок
#
# зафиксировать, кто играет крестиками, а кто - ноликами:
# задать player_sign и comp_sign - строки: "O" и "X"?
#
#
