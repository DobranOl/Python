# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.

def my_func(num_1, num_2, num_3):
    list = [num_1, num_2, num_3]
    max_num = max(list)
    list.remove(max_num)
    max_num_2 = max(list)
    print(f'Sum of 2 max num: {max_num + max_num_2}')

my_func(int(input("Enter 1st number: ")),int(input("Enter 2nd number: ")),int(input("Enter 3rd number: ")))


