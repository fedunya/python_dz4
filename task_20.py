# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

def read_file(file):
    with open(file, 'r') as data:
        a = data.read()
    return a

polinom1 = read_file('file_pol1.txt')
polinom2 = read_file('file_pol2.txt')
polinom1 = polinom1.replace('= 0', '')
with open('file_sum.txt', 'w') as data:
    data.write(f'{polinom1}+ {polinom2}')
