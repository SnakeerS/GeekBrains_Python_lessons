# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб)
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('domashka5_6.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    total_hours = 0
    for line in lines:
        name,hours_lec,hours_pr,hours_lab = list(map(str, line.split()))
        if hours_lec == '-':
            continue
        else:
            hours_lec = int(hours_lec[0:-3])
            total_hours = total_hours + hours_lec
        if hours_pr == '-':
            continue
        else:
            hours_pr = int(hours_pr[0:-4])
            total_hours = total_hours + hours_pr
        if hours_lab == '-':
            continue
        else:
            hours_lab = int(hours_lab[0:-5])
            total_hours = total_hours + hours_lab
        print(total_hours)
        