# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

def user_input(a):
    num = input(a)
    while not num.isdigit() or num == '0':
        print('Неверный ввод, повторите!')
        num = input(a)
    num = int(num)
    return num

import os
os.system("cls")
num = user_input('Введите натуральное число: ')
factors = []
d = 2
while d * d <= num:
        if num % d == 0:
            factors.append(d)
            num//=d
        else:
            d += 1
factors.append(num)
factors = list(set(factors))
print(factors)
