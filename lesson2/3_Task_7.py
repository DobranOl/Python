# В программу должна попадать строка из слов,
# разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

def change_letter():
    words = input('Enter word in lower case: ').split(' ')
    for word in words:
        if word.isascii() is False:
            pass
        else:
            print(word.title())

change_letter()