# Игра "крестики - нолики".

import random
import os

def cls():          # очистка экрана
    os.system('cls')

def checkField(x, y):                   # проверяет, свободно ли поле (x, y)
    if game_field[x][y] == '[ ]':       # если клетка пустая, то
        return True

def doCompMove(x, y):                   # выполняет ход компьютера на (x, y)
    game_field[x][y] = '[O]'            # сделать ход
    comp_moves.append((x, y))           # записать ход компьютера

def compMove():
    """
    Ход компьютера. Случайные координаты поля.
    """
    global turn
    quantity = 1    # нужно сделать 1 ход
    while quantity:
        coord_x = random.randint(0, 2)
        coord_y = random.randint(0, 2)
        if not checkField(coord_x, coord_y):
            continue
        else:
            doCompMove(coord_x, coord_y)
            quantity -= 1
    print('Компьютер сделал ход на клетку ({}, {}):'.
            format(coord_x + 1, coord_y + 1))
    showBoard()
    turn = 1        # флаг перехода хода к игроку

def comp_next_pl():         #  сырая, потестить
    """
    Анализирует ходы противника и определяет координаты поля, 
    которое нужно занять, чтобы не дать ему выиграть.
    Работает, если число сделанных противником ходов >= 2.
    Возвращает кортеж с координатами поля: (x, y), если есть.
    """
    temp = []           # времянка
    next_moves = []     # список потенциальных будущих ходов
    
    for item in coords:
        for i in range(len(player_moves)):
            if player_moves[i] in list(item):
                temp.append(tuple(set(player_moves)&(item)))
    temp = set(temp)    # удаляем дубликаты
    for item in coords:
        for x in temp:        
            if len(item - set(x)) == 1:
                next_moves.append(item - set(x))  
    try:
        result = list(next_moves)
    except:
        result = False
    return result
    
def playerMove():
    """
    Ход игрока.
    """    
    global turn
    print('Ход Игрока ("крестики"):')
    coord_x = int(input('Введите координату Х своего хода (от 1 до 3): ')) - 1
    coord_y = int(input('Введите координату Y своего хода (от 1 до 3): ')) - 1
    if game_field[coord_x][coord_y] == '[ ]':      # если клетка пустая, то
        game_field[coord_x][coord_y] = '[X]'       # сделать ход
        player_moves.append((coord_x, coord_y))    # записать ход игрока
        cls()
        turn = 0    # флаг перехода хода к компьютеру
    else:
        print(str('\n') + 'Эта клетка занята, выберите другую!' + str('\n'))
        playerMove()
    
def whoIsNext():
    """
    Кто ходит следующим?
    """
    return compMove() if turn == 0 else playerMove()

def showBoard():
    """
    Отображение текущего состояния игрового поля.
    """
    print()    
    for i in range(3):
        for j in range(3):
            print(game_field[j][i], end="  ")
        print('\n')

def checkBingo(moves):
    """
    Проверка - а не выиграл ли кто-нибудь?
    Ф-я принимает список ходов.
    """
    for item in coords:
        if item & set(moves) == item:
            return True


game_field = [['[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]'], 
                ['[ ]', '[ ]', '[ ]']]   # инициализация пустого игрового поля
coords = ({(0,0), (1,0), (2,0)}, {(0,1), (1,1), (2,1)}, {(0,2), (1,2), (2,2)},
        {(0,0), (0,1), (0,2)}, {(1,0), (1,1), (1,2)}, {(2,0), (2,1), (2,2)},
        {(0,0), (1,1), (2,2)}, {(0,2), (1,1), (2,0)})
turn = random.randint(0, 1)    # случайное определение очередности первого хода
comp_moves = []         # координаты ходов компьютера
player_moves = []       # координаты ходов игрока

print('******* ИГРА КРЕСТИКИ - НОЛИКИ *******')
showBoard()             # показать пустое игровое поле
input('Нажми любую клавишу чтобы начать игру ')
cls()

for i in range(9):      # основной цикл игры, максимум - 9 ходов 
    whoIsNext()   
    if len(comp_moves) >= 3 or len(player_moves) >= 3:
        if checkBingo(comp_moves):       # проверка победы компьютера
            cls()
            print('Компьютер ("нолики") победил!')
            showBoard()
            break
        elif checkBingo(player_moves):   # проверка победы игрока
            cls()
            print('Игрок ("крестики") победил!')
            showBoard()
            break
        elif (i == 8                     # проверка условия ничьи
            and not checkBingo(comp_moves) and not checkBingo(player_moves)):
            cls()
            print('Ничья!')
            showBoard()
