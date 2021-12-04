# Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль

def new_fact (num_1, num_2):
    if num_2 != 0:
        print(num_1 / num_2)
    else:
        print("Division by zero is not possible!")

new_fact(int(input("Enter 1st number: ")), int(input("Enter 2nd number: ")))