# Реализовать программу работы с органическими клетками,
# состоящими из ячеек.

# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме
# ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки.
# Операцию необходимо выполнять только если разность
# количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное
# деление количества ячеек этих двух клеток.

# В классе необходимо реализовать метод make_order(),
# принимающий экземпляр класса и количество ячеек в ряду.

class Cell:

    def __init__(self, cell_num):
        self.cell_num = cell_num

    def show_cells(self):
        cells = "*" * self.cell_num
        return cells

    def __add__(self, other):
        cell_num = self.cell_num + other.cell_num
        return cell_num

    def __mul__(self, other):
        cell_num = self.cell_num * other.cell_num
        return cell_num

    def __sub__(self, other):
        if self.cell_num > other.cell_num:
            cell_num = self.cell_num - other.cell_num
            return cell_num
        else:
            print('The number of cell particles can`t be less then O!!')

    def __floordiv__(self, other):
        if other != 0:
            cell_num = self.cell_num // other.cell_num
        else:
            print("Division on zero is impossible!")
        return cell_num

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.cell_num / cells_in_row)):
            row += f'{"*" * cells_in_row} \n'
        row += f'{"*" * (self.cell_num % cells_in_row)}'
        return row


cell_1 = Cell(10)
cell_2 = Cell(6)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 // cell_2)
print(cell_1 * cell_2)
print(cell_1.make_order(4))



