# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл

with open('domashka5_4_eng.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    out_f = open('domashka5_4_rus.txt', 'w', encoding='utf8')
    for line in lines:
        numeral,defis,count = list(map(str, line.split()))
        count = int(count)
        if count == 1:
            numeral = 'Один'
        elif count == 2:
            numeral = 'Два'
        elif count == 3:
            numeral = 'Три'
        elif count == 4:
            numeral = 'Четыре'
        # elif count == 5:
        #     numeral = 'Пять'
        # elif count == 6:
        #     numeral = 'Шесть'
        # elif count == 7:
        #     numeral = 'Семь'
        # elif count == 8:
        #     numeral = 'Восемь'
        # elif count == 9:
        #     numeral = 'Девять'
        # elif count == 0:
        #     numeral = 'Ноль'
        out_f.writelines('{} {} {}\n'.format(numeral,defis,count))
    out_f.close()
