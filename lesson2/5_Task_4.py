# Создать (не программно) текстовый файл со следующим содержимым:
# Необходимо написать программу,
# открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл

with open("Task_4.txt", "r") as n:
    nums = {}
    ukr_n = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Чотири'}
    for line in n:
        nums.update({int(line.split(" - ")[1]): line.split(" - ")[0]})
    for key in nums.keys():
        nums[key] = ukr_n[key]
    with open("Task_4_result.txt", "w") as w:
        for key, val in nums.items():
            w.writelines(f"{val} - {key}\n")



