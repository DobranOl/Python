# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
from itertools import count, cycle

give_me_s_num = int(input('Enter starting number: '))
give_me_f_num = int(input('Enter ending number: '))
cycle_list = list('see below'.upper())
def count_():
    count_list = []
    for el in count(give_me_s_num):
        if el > give_me_f_num:
            break
        else:
            count_list.append(el)
    return print(count_list)