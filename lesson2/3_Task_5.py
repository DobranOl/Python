# Программа запрашивает у пользователя строку чисел,
# разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к
# уже подсчитанной сумме.

def ask_for_num():
    global code_word
    print('Enter numbers separated with space.\nIf you want to stop the program, type - stop')
    data = input('Enter numbers: ').split(" ")
    for i in data:
        if i == 'stop':
            data.remove('stop')
            code_word = 1
        else:
            code_word = 0
    new_data = list(map(int, data))
    return new_data

def main():
    database = []
    while True:
        database.append(ask_for_num())
        if code_word == 1:
            sum_of_num = map(sum, database)
            result = sum(sum_of_num)
            print(f'Sum of numbers: {result}\nThe end of program!')
            break
        else:
            sum_of_num = map(sum, database)
            result = sum(sum_of_num)
            print(f'Sum of numbers: {result}')
main()








