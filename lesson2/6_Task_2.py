# Реализовать класс Road (дорога), в котором определить
# атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании
# экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта
# для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна.
# Проверить работу метода.
class Road:

    def __init__(self, __length, __width):
        self.__length = __length
        self.__width = __width

    def count_asphalt(self):
        self.weight = 25
        self.tickness = 5 #tichness of asphalt
        asphalt = self.__length * self.__width * self.tickness * self.weight / 100
        print(f'You will {round(asphalt, 2)} ton of asphalt')


new_road = Road(5000, 5)
new_road.count_asphalt()