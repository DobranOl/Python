# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.
seasons = {'Spring': [3, 4, 5],
           'Summer': [6, 7, 8],
           'Autumn': [9, 10, 11],
           'Winter': [12, 1, 2],
           }
choice = int(input("Enter the the month`s number: "))
for key, value in seasons.items():
    if choice in value:
        print(f'This is {key} season.')



