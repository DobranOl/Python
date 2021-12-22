# Создайте собственный класс-исключение, который должен
# проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Запрашивать у пользователя данные и заполнять список необходимо
# только числами. Класс-исключение должен контролировать типы
# данных элементов списка.

class OnlyNumbers():

    @classmethod
    def check_num(cls):
        print(
            f"Enter number and press Enter to continue.\nPress Q to stop programm.\nEnter S to show the list of numbers")
        list_user = []
        while True:
            user_d = input("Enter number or Q: ")
            if user_d != "Q":
                try:
                    number = list_user.append(int(user_d))
                except ValueError:
                    try:
                        number = list_user.append(float(user_d))
                    except ValueError:
                        print('!!!Please enter a valid number!!!')
            else:
                print(list_user)
                print('The end of program!')
                break


OnlyNumbers.check_num()


