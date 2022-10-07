# Вычислить число c заданной точностью d



import os, math
os.system("cls")
num = input('Введите требуемую точность числа (пример, 0.0001):')
print(f'Число π с заданной точностью {round(math.pi, len(num) - 2)}')
