# Программа принимает действительное положительное число
# x и целое отрицательное число y.
# Выполните возведение числа x в степень y.
# Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.

def power():
    x = int(input('Enter positive integer: '))
    y = int(input('Enter negative integer: '))
    if y < 0:
        x = 1 / x
        y = -y
    result = 1
    while y > 0:
        result = result * x
        y = y - 1
    print(result)

power()

