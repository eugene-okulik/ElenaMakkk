import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)
print('1. Создайте студента (student): ')
data = cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES ('Елена', 'Маковская', NULL)")
student_id = cursor.lastrowid
cursor.execute(f'SELECT * from students where id = {student_id}')
print(cursor.fetchone())
print(' ')

print('2. Создайте несколько книг (books) и укажите, что ваш созданный студент взял их')
query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    query, [
        ('book1', student_id),
        ('book1', student_id),
        ('book1', student_id)
    ]
)
cursor.execute(f'SELECT * from books where taken_by_student_id = {student_id}')
print(cursor.fetchall())
print(' ')

print('3. Создайте группу (group) и определите своего студента туда')
query = "INSERT INTO `groups` (title, end_date, start_date) VALUES (%s, %s, %s)"
cursor.execute(query, ('group', 2025, 2026))
group_id = cursor.lastrowid
cursor.execute(f'SELECT * from `groups` where id = {group_id}')
print(cursor.fetchall())

cursor.execute(f"UPDATE students s SET group_id = {group_id} WHERE s.id = {student_id}")
cursor.execute(f'SELECT * from students where id = {student_id}')
print(cursor.fetchall())
print(' ')

print('4. Создайте несколько учебных предметов (subjects)')
cursor.execute("INSERT INTO subjects (title) VALUES ('subject1')")
subject_id1 = cursor.lastrowid
cursor.execute(f'SELECT * from subjects where id = {subject_id1}')
print(cursor.fetchall())

cursor.execute("INSERT INTO subjects (title) VALUES ('subject2')")
subject_id2 = cursor.lastrowid
cursor.execute(f'SELECT * from subjects where id = {subject_id2}')
print(cursor.fetchall())

cursor.execute("INSERT INTO subjects (title) VALUES ('subject3')")
subject_id3 = cursor.lastrowid
cursor.execute(f'SELECT * from subjects where id = {subject_id3}')
print(cursor.fetchall())
print(' ')

print('5. Создайте по два занятия для каждого предмета (lessons)')
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('lesson1', {subject_id1})")
lesson_1 = cursor.lastrowid
cursor.execute(f'SELECT * from lessons where id = {lesson_1}')
print(cursor.fetchall())

cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('lesson2', {subject_id1})")
lesson_2 = cursor.lastrowid
cursor.execute(f'SELECT * from lessons where id = {lesson_2}')
print(cursor.fetchall())

cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('lesson1', {subject_id2})")
lesson_3 = cursor.lastrowid
cursor.execute(f'SELECT * from lessons where id = {lesson_3}')
print(cursor.fetchall())

cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('lesson2', {subject_id2})")
lesson_4 = cursor.lastrowid
cursor.execute(f'SELECT * from lessons where id = {lesson_4}')
print(cursor.fetchall())

cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('lesson1', {subject_id3})")
lesson_5 = cursor.lastrowid
cursor.execute(f'SELECT * from lessons where id = {lesson_5}')
print(cursor.fetchall())

cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('lesson2', {subject_id3})")
lesson_6 = cursor.lastrowid
cursor.execute(f'SELECT * from lessons where id = {lesson_6}')
print(cursor.fetchall())
print(' ')

print('6. Поставьте своему студенту оценки (marks) для всех созданных вами занятий')
query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    query, [
        (5, lesson_1, student_id),
        (5, lesson_2, student_id),
        (5, lesson_3, student_id),
        (5, lesson_4, student_id),
        (5, lesson_5, student_id),
        (5, lesson_6, student_id)
    ]
)
cursor.execute(f'SELECT * from marks where student_id = {student_id}')
print(cursor.fetchall())
print(' ')

print('7. Получите информацию из базы данных: \n'
      'Все оценки студента\n'
      'Все книги, которые находятся у студента\n'
      'Для вашего студента выведите всё, что о нем есть в базе: группа, книги, \n'
      'оценки с названиями занятий и предметов (всё одним запросом с использованием Join)')

cursor.execute(f"SELECT m.value FROM marks m where m.student_id = {student_id}")
print(cursor.fetchall())

cursor.execute(f"SELECT b.title from books b where b.taken_by_student_id = {student_id}")
print(cursor.fetchall())

cursor.execute(f"SELECT st.name, st.second_name, g.title, b.title, m.value, s.title, l.title "
               f"from students st "
               f"JOIN `groups` g ON st.group_id = g.id "
               f"JOIN books b ON st.id = b.taken_by_student_id "
               f"JOIN marks m ON m.student_id = st.id "
               f"JOIN lessons l ON l.id = m.lesson_id "
               f"JOIN subjects s ON s.id = l.subject_id "
               f"where st.id = {student_id}")
print(cursor.fetchall())

db.commit()
db.close()
