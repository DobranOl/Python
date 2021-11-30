# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове
sentence = input("Enter sentence: ").split(" ")
for ind, words in enumerate(sentence, 1):
    if len(words) > 10:
        print(ind, words[:11])
    else:
        print(ind, words)
