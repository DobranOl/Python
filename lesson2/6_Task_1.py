# Создать класс TrafficLight (светофор).
#
# - определить у него один атрибут color (цвет) и
# метод running (запуск);
# - атрибут реализовать как приватный;
# - в рамках метода реализовать переключение светофора
# в режимы: красный, жёлтый, зелёный;
# - продолжительность первого состояния (красный) составляет
# 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# - переключение между режимами должно осуществляться
# только в указанном порядке (красный, жёлтый, зелёный);
# - проверить работу примера, создав экземпляр и
# вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и
# завершать скрипт.
import time
class TrafficLight:

    color_time = {'Red': 7,
               'Yellow': 2,
               'Green': 6,
               }
    __color = None
    __color_i = 0 # index  of colors in dictionary above
    change_c_c = 3 # change 3 time if not set

    def __init__(self, start_col='Red', change_c_c=3):
        self.__color = start_col if self.color_time.get(start_col) else list(self.color_time.keys())[self.__color_i]
        self.__color_i =list(self.color_time.keys()).index(self.__color)
        self.change_c_c = change_c_c

    def running(self):
        print(self.__color)
        while self.change_c_c:
            time.sleep(self.color_time.get(self.__color))
            self.__color_i = (self.__color_i + 1) % 3
            self.__color = list(self.color_time.keys())[self.__color_i]
            print(self.__color)
            self.change_c_c -= 1


t_light = TrafficLight('Yellow', 5)
t_light.running()