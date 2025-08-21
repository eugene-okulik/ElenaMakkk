# Второй класс
# Создайте дочерний класс для первого. Это будет класс для школьных учебников. В нем будут дополнительные атрибуты:
#
# предмет (типа математика, история, география),
# класс (школьный класс, для которого этот учебник)(осторожно с названием переменной. class - зарезервированное слово),
# наличие заданий (bool)
# Создайте несколько экземпляров учебников.
# После создания пометьте один учебник как зарезервированный.
# Распечатайте детали о каждом учебнике в таком виде: Если учебник зарезервирован:
#
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9, зарезервирована
# если не зарезервирован:
#
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9
from homework.elena_makovskaya.hw_lesson_11.task_1 import Book


class School_book(Book):
    def __init__(self, name_book, author, pages_count, isbn, subject, group, hw):
        super().__init__(name_book, author, pages_count, isbn)
        self.subject = subject
        self.group = group
        self.hw = hw


school_book_1 = School_book('Геометрия для 9-х классов', 'Пифагор', 500,
                            5554, 'Математика', 9, True)
school_book_2 = School_book('История Египта', 'Александров', 773,
                            5554, 'Всемирная история', 9, True)
school_book_3 = School_book('Русский язык для 9х классов', 'Сахарчук', 556,
                            5554, 'Русский язык', 9, False)
school_book_4 = School_book('Физика для 9х классов', 'Иванов', 507,
                            5554, 'Физика', 9, True)
school_book_5 = School_book('Информатика для 9х классов', 'Петров', 598,
                            5554, 'Информатика', 9, True)

school_book_4.is_reserved = True

school_books = [school_book_1, school_book_2, school_book_3, school_book_4, school_book_5]

for school_book in school_books:
    if school_book.is_reserved:
        print(f'Название: {school_book.name_book}, Автор: {school_book.author}, страниц: {school_book.pages_count},'
              f' предмет: {school_book.subject}, класс: {school_book.group},зарезервирована')
    else:
        print(f'Название: {school_book.name_book}, Автор: {school_book.author}, страниц: {school_book.pages_count}, '
              f'предмет: {school_book.subject}, класс: {school_book.group}')
