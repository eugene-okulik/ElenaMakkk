#Напишите программу, которая перебирает последовательность от 1 до 100.
# Для чисел кратных 3 она должна написать: "Fuzz" вместо печати числа, а для чисел кратных 5 печатать "Buzz".
# Для чисел которые кратны одновременно и 3 и 5 надо печатать "FuzzBuzz". Иначе печатать число.

numbers = range(1, 101)
for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        print("FuzzBuzz")
    elif number % 3 == 0:
        print("Fuzz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
