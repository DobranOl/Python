#  Создать текстовый файл (не программно),
#  построчно записать фамилии сотрудников и величину их окладов.
#  Определить, кто из сотрудников имеет оклад менее 20 тыс.,
#  вывести фамилии этих сотрудников.
#  Выполнить подсчет средней величины дохода сотрудников.

with open("task_3.txt", "r") as f:
    data = dict()
    good_s = []
    line_i = 0
    for line in f:
        data.update({line.split(" ")[0]: int(line.split(" ")[1])})
        line_i += 1
    for name, salary in data.items():
        if int(salary) > 1000:
            good_s.append(name)
middle = sum(data.values())/line_i
print(f'List of employees with salary greater then 1000$\n{good_s}\nAverage salary - {round(middle, 2)}')

