
-- 1. Создайте студента (student)
INSERT INTO students (name, second_name, group_id)
VALUES ('Elena', 'Makouskaya', 1)

SELECT * from students
where name = 'Elena'
AND second_name = 'Makouskaya'

-- 2. Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
INSERT INTO books  (title)
VALUES
('the best python tutorial'),
('the mid python tutorial'),
('the worst python tutorial')

SELECT * from books b
where title = 'the best python tutorial'
OR title = 'the mid python tutorial'
OR title = 'the worst python tutorial'

UPDATE books b
SET taken_by_student_id = 21130
WHERE id = 2505 OR id = 2506 OR id = 2507

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
