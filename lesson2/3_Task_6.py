# Реализовать функцию int_func(),
# принимающую слова из маленьких латинских букв
# и возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

def change_letter():
    word = input('Enter word in lower case: ')
    if word.isascii() is True:
        print(word.title())
    else:
        print('Enter word with latin character!')

change_letter()

