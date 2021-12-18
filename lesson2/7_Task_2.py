# Реализовать проект расчета суммарного расхода ткани на производство
# одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто)
# и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.

# Для определения расхода ткани по каждому типу одежды
# использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3).
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_need(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    def fabric_need(self):
        result = self.size / 6.5 + 0.5
        print(f'To make your coat you will need {round(result, 2)} sm of fabric')
        return result

class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    def fabric_need(self):
        result = 2 * self.height + 0.3
        print(f'To make your suit you will need {round(result, 2)} sm of fabric')
        return result

Tom_order = Coat(400)
John_order = Suit(190)

print(f' Total fabric - {round((Tom_order.fabric_need() + John_order.fabric_need()), 2)}')

