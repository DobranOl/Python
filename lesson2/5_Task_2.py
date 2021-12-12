# Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк,
# количества слов в каждой строке.
with open ("task_2.txt", "r") as BTS:
    line_c = 0
    for i, line in enumerate(BTS, start= 1):
        split_ = line.split(" ")
        count_w = len(split_)
        print(f'In {i} line - {count_w} word(s)')
        line_c += 1

print(f'Total number of lines - {line_c}')




