# Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число
#
# На всякий случай, напомню, что превращать результат работы генератора в список - неправильно.

import sys
sys.set_int_max_str_digits(0)


def fibonacci_numbers(limit=100000):
    num_1 = 0
    num_2 = 1
    counter = 1
    while counter < limit:
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2
        counter += 1


count = 1
for nums in fibonacci_numbers(100001):
    if count == 5:
        print(nums)
    elif count == 200:
        print(nums)
    elif count == 1000:
        print(nums)
    elif count == 100000:
        print(nums)
    count += 1
