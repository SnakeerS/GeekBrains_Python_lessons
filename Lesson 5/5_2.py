#Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке

with open('domashka5_2.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    i = 1
    for line in lines:
        print('Строка {}, количество символов {}'.format(i,len(line.strip())))
        i += 1
