#  Создать (программно) текстовый файл, записать в него программно
#  набор чисел, разделенных пробелами.
#  Программа должна подсчитывать сумму чисел в файле
#  и выводить ее на экран.
user_d = input("Enter numbers: ")
with open("Task_5", "w+") as nums:
    nums.writelines(user_d)
    nums.seek(0)
    str_n = nums.read()
    list_ = [int(el) for el in str_n.split(" ")]
    summary = sum(list_)

print(f'Sum of numbers: {summary}')

