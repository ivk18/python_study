# Игра "крестики - нолики".

from random import randint
import os


def compMove():
    """
    Ход компьютера.
    """
    global turn
    quantity = 1    # сделать 1 ход
    while quantity:
        coord_x = randint(0, 2)
        coord_y = randint(0, 2)
        if game_field[coord_x][coord_y] == '[ ]':  # если клетка пустая, то
            game_field[coord_x][coord_y] = '[O]'   # сделать ход
            comp_moves.append((coord_x, coord_y))  # записать ход компьютера
            quantity -= 1    
    print('Компьютер сделал ход на клетку ({}, {}):'.format(coord_x + 1, 
            coord_y + 1))
    showBoard()
    turn = 1    # флаг перехода хода к игроку

def playerMove():
    """
    Ход игрока.
    """
    global turn
    coord_x = int(input('Введите координату Х своего хода (от 1 до 3): ')) - 1
    coord_y = int(input('Введите координату Y своего хода (от 1 до 3): ')) - 1
    if game_field[coord_x][coord_y] == '[ ]':  # если клетка пустая, то
        game_field[coord_x][coord_y] = '[X]'  # сделать ход
        player_moves.append((coord_x, coord_y))  # записать ход игрока
        showBoard()
        turn = 0     # флаг перехода хода к компьютеру
    else:
        print(str('\n') + 'Эта клетка занята, выберите другую!' + str('\n'))
        playerMove()
    
def whoIsNext():
    """
    Кто ходит следующим?
    """
    if turn == 0:
        print('Ходит Компьютер ("нолики"):')
        compMove()
    else:
        print('Ходит Игрок ("крестики"):')
        playerMove()

def showBoard():
    """
    Отображение текущего состояния игрового поля.
    """
    print()
    # os.system('cls')      # очистить экран
    for i in range(3):
        for j in range(3):
            print(game_field[j][i], end="  ")
        print('\n')

def checkBingo(moves): # принимает список ходов
    """
    Проверка - а не выиграл ли кто-нибудь?
    """
    moves_list = moves[:]
    start_item = moves_list[0]
    moves_list = moves_list[1:]
    while moves_list:
        for item in moves_list:
            #  ПРОВЕРИТЬ УСЛОВИЯ ПОБЕДЫ
            if (start_item[0] == item[0] or start_item[1] == item[1] or
                abs(start_item[0] - item[0]) == abs(start_item[1] - item[1])):
                bingo = True
        start_item = moves_list[0]
        moves_list = moves_list[1:]


game_field = [['[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]'], 
                ['[ ]', '[ ]', '[ ]']]   # инициализация пустого игрового поля
turn = randint(0, 1)    # определение очередности первого хода
bingo = False       # пока еще никто не выиграл
comp_moves = []     # координаты ходов компьютера
player_moves = []   # координаты ходов игрока

print('******* ИГРА НАЧАЛАСЬ! *******')
showBoard()     # показать пустое игровое поле

for i in range(9):   # основной цикл игры, максимум - 9 ходов
    whoIsNext()
    if len(comp_moves) >= 3 or len(player_moves) >= 3:
        checkBingo(comp_moves)      # проверка на выигрыш компьютера
        checkBingo(player_moves)    # проверка на выигрыш игрока
