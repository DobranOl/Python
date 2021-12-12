# Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.

# Необходимо построчно прочитать файл,
# вычислить прибыль каждой компании,
# а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.

# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь
# (со значением убытков).
import json
with open('Task_7.txt', "r") as comp:
    company = {}
    average = 0
    count = 1
    for line in comp:
        company.update({line.split(" ")[0]: int(int(line.split(" ")[2]) - int(line.split(" ")[3]))})
    for val in company.values():
        if val > 0:
            average = (average + val)/count
            count += 1
    company.update({'Average': round(average, 2)})

with open('Task_7_res.json', 'w') as res:
    json.dump(company, res)

print(company)


