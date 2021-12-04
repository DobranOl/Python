# Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.
def show_list(list):
    user_data = {}
    for item in list:
        user_data[item] = input(f"Enter your {item}: ")
    return user_data

def main():
    database = []
    list = ('Name', 'Surname', 'email', 'cell number', 'year of birth', 'city')
    while True:
        database.append(show_list(list))
        print(database)

main()