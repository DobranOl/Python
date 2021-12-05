# Реализовать скрипт, в котором должна быть предусмотрена функция
# расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать
# скрипт с параметрами.

from sys import argv
script, time, rate, premium = argv

def salary ():
    salary = (float(time) * float(rate)) + float(premium)
    return salary

print(f"The employee`s salary - {salary()}")

