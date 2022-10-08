# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def user_input(a):
    num = input(a)
    while not num.isdigit() or num == '0':
        print('Неверный ввод, повторите!')
        num = input(a)
    num = int(num)
    return num

import os, random
os.system("cls")
k = user_input('Введите натуральную степень: ')
polynomial = ''
while k > 0:
    coefficient = random.randint(0, 100)    
    if coefficient > 0:
        if k > 1: polynomial += f'{coefficient}x^{k} + '
        elif k == 1: polynomial += f'{coefficient}x + '
    k = k - 1
coefficient = random.randint(0, 1)
if coefficient > 0: polynomial += f'{coefficient}'
else: polynomial = polynomial[:len(polynomial) - 4] # удаление лишнего ' + '
polynomial += ' = 0'
with open('file.txt', 'w') as data:
    data.write(polynomial)
