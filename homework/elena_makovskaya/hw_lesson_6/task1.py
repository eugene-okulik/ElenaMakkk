# Напишите программу, которая добавляет ‘ing’ в конец слов (к каждому слову) в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
# Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”
# и после этого выводит получившийся текст на экран. Знаки препинания не должны оказаться внутри слова.
# Если после слова идет запятая или точка, этот знак препинания должен идти после того же слова,
# но уже преобразованного.
from test.libregrtest.utils import printlist
from test.test_inspect.inspect_fodder2 import replace

text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, "
        "dignissim vitae libero")

words = text.split()
result_words = []

for word in words:
    if word.endswith(('.', ',')):
        new_words = word[:-1] + 'ing' + '.'
    else:
        new_words = word + 'ing'

    result_words.append(new_words)

print(' '.join(result_words))
