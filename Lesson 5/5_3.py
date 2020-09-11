# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('domashka5_3.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    average_salary = 0
    total_salary = 0
    i = 0
    for line in lines:
        name,salary = list(map(str, line.split()))
        salary = float(salary)
        total_salary = total_salary + salary
        i += 1
        average_salary = total_salary / i
        if salary < 20000.00:
            print(name)

    print('Средняя зарплата составила {} рублей.'.format(average_salary))




