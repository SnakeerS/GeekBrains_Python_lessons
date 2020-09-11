# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('domashka5_5.txt', 'w', encoding='utf-8') as f:
    text_list = 0
    sum = 0
    while text_list != '':
        text_list = input()
        if text_list == '':
            break
        else:
            text_list = int(text_list)
            sum = sum + text_list
            f.write('{} '.format(str(text_list)))
print(sum)