'''
Сортировка словарей. 

Cловари представляют собой неупорядоченные коллекции. 
Напишите цикл for, который выводит элементы словаря в порядке возрастания. 
(Подсказка: используйте метод keys словаря и метод списка sort 
или новую встроенную функцию sorted.)
'''

D = dict(k='asdf', p=45, q='ssa', d='qwe', a='rty', n=12)
print('Unsorted dict:\n' + str(D) + '\n')

print('Elements of sorted dict:')
for x in sorted(D):
    print((x, D[x]), end=' ')
    
print('\n')
