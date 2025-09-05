
-- 1. Создайте студента (student)
INSERT INTO students (name, second_name, group_id)
VALUES ('Elena', 'Makouskaya')

SELECT * from students
where name = 'Elena'
AND second_name = 'Makouskaya'

-- 2. Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
INSERT INTO books  (title, taken_by_student_id)
VALUES ('the best python tutorial', 21130)

INSERT INTO books  (title, taken_by_student_id)
VALUES ('the mid python tutorial', 21130)

INSERT INTO books  (title, taken_by_student_id)
VALUES ('the worst python tutorial', 21130)

SELECT * from books b
where taken_by_student_id = 21130


-- 3. Создайте группу (group) и определите своего студента туда
INSERT INTO `groups`  (title, end_date, start_date)
VALUES ('Авто', '2026', '2025')

SELECT * from `groups` g
where g.title = 'Авто'
AND g.end_date = '2026'
AND g.start_date = '2025'

UPDATE students s
SET group_id = 5645
WHERE s.id = 21130

SELECT * FROM students s
WHERE s.id = 21130

-- 4. Создайте несколько учебных предметов (subjects)
INSERT INTO subjects(title)
VALUES
('sub 1'),
('sub 2'),
('sub 3')

SELECT * FROM subjects s
where s.title  = 'sub 1' OR s.title  = 'sub 2' OR s.title  = 'sub 3'

-- 5. Создайте по два занятия для каждого предмета (lessons)
INSERT INTO lessons (title, subject_id)
VALUES
('lesson 1', 11948),
('lesson 2', 11948),
('lesson 1', 11949),
('lesson 2', 11949),
('lesson 1', 11950),
('lesson 2', 11950)

SELECT * FROM lessons l
where l.subject_id = 11948
OR l.subject_id = 11949
OR l.subject_id = 11950

-- 6. Поставьте своему студенту оценки (marks) для всех созданных вами занятий
INSERT INTO marks (value, lesson_id, student_id)
VALUES
(10, 12179, 21130),
(10, 12180, 21130),
(10, 12181, 21130),
(10, 12182, 21130),
(10, 12183, 21130),
(10, 12184, 21130)

SELECT * from marks m
where m.student_id = 21130



-- Получите информацию из базы данных:
-- Все оценки студента
-- Все книги, которые находятся у студента
-- Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
-- (всё одним запросом с использованием Join)

SELECT m.value FROM marks m
where m.student_id = 21130

SELECT b.title from books b
where b.taken_by_student_id = 21130


SELECT st.name, st.second_name, g.title, b.title, m.value, s.title, l.title
from students st
JOIN `groups` g ON st.group_id = g.id
JOIN books b  ON st.id = b.taken_by_student_id
JOIN marks m  ON m.student_id = st.id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjects s ON s.id = l.subject_id
where st.id = 21130
