# Реализовать генератор с помощью функции с
# ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом:
# for el in fact(n).
# Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.
from itertools import count
from functools import reduce
n = int(input('Enter inger: '))
def fact(n):
    for el in range(1, n+1):
        facterial_trash = []
        for nums in range(1, el+1):
            facterial_trash.append(nums)
        facterial = reduce(lambda x, y: x * y, facterial_trash)
        yield facterial


facterial = fact(n)

for el in facterial:
    print(el)

