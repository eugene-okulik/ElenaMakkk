# В папке /homework/eugene_okulik/Lesson_16/hw_data лежит csv файл. Файл никуда не копируйте и не переносите.
# Прочитайте этот файл с помощью модуля csv и проверьте есть ли те данные, которые там перечислены, в нашей базе данных.
#
# При подключении к базе данных не прописывайте данные подключения в коде,
# а воспользуйтесь подходом .env c такими переменными: DB_USER, DB_PASSW, DB_HOST, DB_PORT, DB_NAME.
# Я на своем компе уже создал файл .env с этими переменными, так что, если все сделаем одинаковые названия,
# будет работать всё универсально
#
# В результате сравнения, если обнаружится, что каких-то данных, которые есть в файле, нет в базе данных,
# распечатайте каких данных не хватает в базе.
#
# Подсказка для самопроверки: в базе нет данных, которые полностью соответствуют первой строке файла,
# но в базе есть данные, которые соответствуют второй строке файла.


import csv
import os
import dotenv
import mysql.connector as mysql

dotenv.load_dotenv(override=True)
db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(eugene_file_path, newline='', encoding='utf-8') as csvfile:
    filedata = csv.DictReader(csvfile)
    for row in filedata:
        name = row['name']
        second_name = row['second_name']
        group_title = row['group_title']
        book_title = row['book_title']
        subject_title = row['subject_title']
        lesson_title = row['lesson_title']
        mark_value = row['mark_value']

        query = """
            SELECT * FROM students st
            JOIN `groups` g ON st.group_id = g.id
            JOIN books b ON st.id = b.taken_by_student_id
            JOIN marks m ON m.student_id = st.id
            JOIN lessons l ON l.id = m.lesson_id
            JOIN subjects s ON s.id = l.subject_id
            WHERE st.name = %s AND st.second_name = %s
            AND g.title = %s AND b.title = %s
            AND s.title = %s AND l.title = %s
            AND m.value = %s
        """
        cursor.execute(
            query,
            (name, second_name, group_title, book_title, subject_title, lesson_title, mark_value)
        )
        result = cursor.fetchall()

        if result:
            pass
        else:
            print(row)
