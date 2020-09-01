# Задание 4: Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите число: '))
max_numeral = 0

while number > 1:
    count_number = number % 10
    if max_numeral < count_number:
        max_numeral = round(count_number,0)
    number = number // 10

print(max_numeral)
