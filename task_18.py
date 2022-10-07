# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов 
# исходной последовательности.

def fill_list_random(list_len):
    return [random.randint(1, 9) for i in range(list_len)]
def user_input(a):
    num = input(a)
    while not num.isdigit() or num == '0':
        print('Неверный ввод, повторите!')
        num = input(a)
    num = int(num)
    return num

import os, random
os.system("cls")
my_list = fill_list_random(user_input('Введите размер списка: '))
print(f'\nЗаданный список -> {my_list}')
print(f'Список неповторяющихся элементов -> {list(set(my_list))}')

