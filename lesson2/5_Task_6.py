#  Необходимо создать (не программно) текстовый файл,
#  где каждая строка описывает учебный предмет и наличие
#  лекционных, практических и лабораторных занятий
#  по этому предмету и их количество.
#  Важно, чтобы для каждого предмета не обязательно были все типы занятий.
#  Сформировать словарь, содержащий название предмета
#  и общее количество занятий по нему.
#  Вывести словарь на экран.
import re
with open("Task_6.txt", "r") as subs:
    subjects_1 = {}
    key_words = ['(lec)', '(practice)', '(lab)', '']
    for line in subs:
        subjects_1.update({line.split(": ")[0]: line.split(": ")[1]})
    for key, val in subjects_1.items():
        subjects_1[key] = re.split(", | |\n", val)
    for val in subjects_1.values():
        for i, item in enumerate(val):
            if item in key_words:
                val.remove(item)
                val.pop(-1)
    for key, val in subjects_1.items():
        subjects_1[key] = sum(list(map(int, val)))


print(subjects_1)

