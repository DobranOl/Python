# Реализуйте базовый класс Car.
# У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала,
# остановилась, повернула (куда).
# Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите
# метод show_speed.
# При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'The {self.color} {self.name} started moving')

    def stop(self):
        print(f'The {self.color} {self.name} stopped moving')

    def turn(self, direction):
        print(f'The {self.color} {self.name} turned {direction}')

    def show_speed(self):
        print(f'The {self.color} {self.name} car have {self.speed} km/h speed')


class TownCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'You reach speed limit!')
        else:
            print(f'The {self.color} {self.name} car have {self.speed} km/h speed')


class SportCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'You reach speed limit!')
        else:
            print(f'The {self.color} {self.name} car have {self.speed} km/h speed')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


tom_car = TownCar(60, 'red', 'Ford')
tom_car.go()
tom_car.show_speed()
tom_car.turn('left')
tom_car.stop()

jerry_car = SportCar(100, 'black', "Ferrari")
jerry_car.go()
jerry_car.show_speed()

maddy_car = WorkCar(30, 'green', 'Opel')
maddy_car.go()
maddy_car.show_speed()
maddy_car.turn('right')

linda_car = PoliceCar(50, 'white', 'Police')
linda_car.go()
linda_car.show_speed()
linda_car.stop()

