# Игра "крестики - нолики".
# что-то поменял
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
    print('Компьютер сделал ход на клетку ({}, {}):'.
            format(coord_x + 1, coord_y + 1))
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
        os.system('cls')      # очистить экран   
        turn = 0     # флаг перехода хода к компьютеру
    else:
        print(str('\n') + 'Эта клетка занята, выберите другую!' + str('\n'))
        playerMove()
    
def whoIsNext():
    """
    Кто ходит следующим?
    """
    if turn == 0:        
        # Ходит Компьютер ("нолики")
        compMove()
    else:        
        print('Сейчас ходит Игрок ("крестики"):')
        playerMove()

def showBoard():
    """
    Отображение текущего состояния игрового поля.
    """
    print()    
    for i in range(3):
        for j in range(3):
            print(game_field[j][i], end="  ")
        print('\n')

def checkBingo(moves): # принимает список ходов
    """
    Проверка - а не выиграл ли кто-нибудь?
    """
    win = ({(0,0), (1,0), (2,0)}, {(0,1), (1,1), (2,1)}, {(0,2), (1,2), (2,2)},
        {(0,0), (0,1), (0,2)}, {(1,0), (1,1), (1,2)}, {(2,0), (2,1), (2,2)},
        {(0,0), (1,1), (2,2)}, {(0,2), (1,1), (2,0)})
    for item in win:
        if item & set(moves) == item:
            return True


game_field = [['[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]'], 
                ['[ ]', '[ ]', '[ ]']]   # инициализация пустого игрового поля
turn = randint(0, 1)    # случайное определение очередности первого хода
comp_moves = []     # координаты ходов компьютера
player_moves = []   # координаты ходов игрока

print('******* ИГРА КРЕСТИКИ - НОЛИКИ *******')
showBoard()     # показать пустое игровое поле
input('Нажми любую клавишу чтобы начать игру ')
os.system('cls')      # очистить экран

for i in range(9):   # основной цикл игры, максимум - 9 ходов    
    if len(comp_moves) >= 3 or len(player_moves) >= 3:
        if checkBingo(comp_moves):      # проверка на выигрыш компьютера
            os.system('cls')      # очистить экран
            print('Компьютер победил!')
            showBoard()
            break
        if checkBingo(player_moves):    # проверка на выигрыш игрока
            os.system('cls')      # очистить экран
            print('Игрок победил!')
            showBoard()
            break
    whoIsNext()
