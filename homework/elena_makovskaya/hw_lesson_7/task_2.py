# Задание №2
# Дан такой словарь:
#
# words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
# Выведите на экран каждый ключ столько раз сколько указано в значении. Т.е. как-то так:
#
# III
# lovelovelovelovelove
# итд
# Cделайте так, чтобы каждый ключ печатался в одной строке (как в примере)
#
# Помните, что копипаст одного и того же кода - плохо


words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for key, values in words.items():
    counter = 0
    while counter < values:
        print(key, end='')
        counter += 1
    print(' ')
