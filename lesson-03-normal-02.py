# урок 03, задание 2 (уровень normal)

# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

__author__ = 'Караваев Илья Викторович'

def sort_to_max(origin_list):
    k = len(origin_list) - 1
    while True:     # после первого прохода в origin_list[k] - max элемент
        for i in range(k):
            if origin_list[i+1] < origin_list[i]:
                buf = origin_list[i+1]            
                origin_list[i+1] = origin_list[i]
                origin_list[i] = buf
            else:
                continue
            # print(str(origin_list), k)    #  для контроля итераций
        if k == 0:
            break
        k -= 1  # после каждого прохода кол-во сравниваемых эл-в сокращается на 1
    return origin_list  # возвращается измененный исходный (!) список

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
