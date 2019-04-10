'''
Основы циклов.

a. Напишите цикл for, который выводит ASCII-коды всех символов в стро-
ке с именем S. Для преобразования символов в целочисленные ASCII-
коды используйте встроенную функцию ord(character). (Поэксперимен-
тируйте с ней в интерактивной оболочке, чтобы понять, как она рабо-
тает.)
b. Затем измените цикл так, чтобы он вычислял сумму кодов ASCII всех
символов в строке.
c. Наконец, измените свой программный код так, чтобы он возвращал но-
вый список, содержащий ASCII-коды всех символов в строке.
'''

string = input('Input any symbols: ')

# a.
print('\nUnicode codes of symbols: ', end='')
for s in string:    
    print(ord(s), end=' ')

# b, c.
summa = 0
sym_list = []
for s in string:
    summa += ord(s)
    sym_list.append(ord(s))
print('\n\nSum of codes = ' + str(summa))
print('\nList of codes: ' + str(sym_list) + '\n')

