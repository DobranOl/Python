# Создайте собственный класс-исключение, обрабатывающий
# ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем.
# При вводе нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDivision(Exception):
    def __str__(self):
        return 'Division by Zero isn`t possible!'


def my_simple_div(num_1, num_2):
    try:
        if num_2 != 0:
            result = num_1 / num_2
            print(f'The division of {num_1} on {num_2} - {result}')
        else:
            raise ZeroDivision()
    except ZeroDivision as err:
        print(err)


print(my_simple_div(12, 0))
# I DON`T UNDERSTAND WHY IT KEEPS PRINT NONE. hELB
print(my_simple_div(1, 2))
