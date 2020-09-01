# Задание 3: Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

print('Скрипт выводит сумму чисел n + nn + nnn')
count_n = input('Введите число "n": ')

count_nn = str(count_n) + str(count_n)
count_nnn = str(count_nn) + str(count_n)

print('')  # для красоты вывода
print('Ваши числа: {}, {}, {}'.format(count_n,count_nn,count_nnn))
print('Ответ:',int(count_n) + int(count_nn) + int(count_nnn))
