#  Реализовать класс Stationery (канцелярская принадлежность)
#  Определить в нем атрибут title (название) и метод draw (отрисовка).
#  Метод выводит сообщение “Запуск отрисовки.”
#  Создать три дочерних класса Pen (ручка), Pencil (карандаш),
#  Handle (маркер).
#  В каждом из классов реализовать переопределение метода draw.
#  Для каждого из классов методы должен выводить
#  уникальное сообщение

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start of drawing')


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
       print(f'Start of drawing with {self.title}')
       print(f'You can draw details of picture')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Item is {self.title}. You can draw details of picture')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Item is {self.title}. You can highlight text')


pen = Pen('pen')
pencil = Pencil('pencil H2')
handle = Handle('yellow handle')
pen.draw()
pencil.draw()
handle.draw()
