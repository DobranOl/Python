# Реализовать класс «Дата», функция-конструктор которого
# должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их
# тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:

    def __init__(self, day_month_year: str):
        self.day_month_year = day_month_year

    @classmethod
    def split_date(cls, day_month_year):
        user_date = day_month_year.split("-")
        int_date = list(map(int, user_date))
        return int_date

    @staticmethod
    def check_date(day: int,month: int,year: int):
        if 1 <= day <= 31 and month < 2022 and 1 <= month <=12:
            return f'{day}:{month}:{year} is correct!'
        else:
            return f'{day}:{month}:{year} isn`t correct! Please check your date.'

print(Date.split_date('31-12-2021'))
print(Date.check_date(12, 3, 2021))
print(Date.check_date(45, 3, 1997))







