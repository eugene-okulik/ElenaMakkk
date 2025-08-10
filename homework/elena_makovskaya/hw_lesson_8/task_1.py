# Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool.
# Спросите у пользователя salary. А bonus пусть назначается рандомом.
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.
# Примеры результатов:
# 10000, True - '$10255'
# 25000, False - '$25000'
# 600, True - '$3785'

import random

def get_salary_with_bonus():
    salary = int(input('Введите вашу зарплату: '))
    bonus = bool(random.getrandbits(1))
    if bonus:
        new_salary = salary + int(random.randrange(0, 1000))
    else:
        new_salary = salary
    print(f'{salary}, {bonus} - ${new_salary}')


get_salary_with_bonus()
