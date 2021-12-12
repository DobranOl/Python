# Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

while True:
    data = input('Enter your data: ')
    try:
        with open('user_data.text', "x") as file:
            file.write(f"{data}")
    except FileExistsError:
        with open('user_data.text', "a") as file:
            file.write(f"\n{data}")
    if data == " ":
        break
