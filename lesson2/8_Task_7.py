# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex():

    def __init__(self, num: complex):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __mul__(self, other):
        return self.num * other.num

    def __sub__(self, other):
        return self.num - other.num

    def __truediv__(self, other):
        return self.num / other.num


a = Complex(complex('1+4j'))
b = Complex(complex('2'))
c = Complex(complex('2.1-2.1j'))
print(a + b)
print(a - b)
print(a * b)
print(a / b)