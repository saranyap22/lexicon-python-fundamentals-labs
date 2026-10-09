---------------------------------------------------

---------DESIGNING GOOD DATABASE-------------------

----- Excercise 16 -----------------

CREATE TABLE students(
student_id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
email TEXT,
city TEXT
);


CREATE TABLE teachers(
teacher_id INTEGER PRIMARY KEY,
name NOT NULL,
email TEXT,
city TEXT

);

CREATE TABLE lessons(
lesson_id INTEGER PRIMARY KEY,
teacher_id INTEGER NOT NULL,
lesson_date TEXT NOT NULL,
lesson_time TEXT NOT NULL,
instrument NOT NULL CHECK (instrument IN ('Piano','Guitar','Flute','Drum','Violin')),
FOREIGN KEY(teacher_id) REFERENCES teachers(teacher_id)
);

CREATE TABLE student_lessons(
student_id INTEGER NOT NULL,
lesson_id INTEGER NOT NULL,
status TEXT CHECK (status IN ('NEW','INPROGRESS','COMPLETED')),
PRIMARY KEY(student_id,lesson_id),
FOREIGN KEY(student_id) REFERENCES students(student_id),
FOREIGN KEY(lesson_id) REFERENCES lessons(lesson_id)
);

------------ Checking db with queries-------------

INSERT INTO students(student_id,name,city,email)
VALUES (1,'sara','solna','sara@gmail.com'), (2,'emil','kista','emil@hotmail.com')
;

INSERT INTO teachers(teacher_id,name,city,email)
VALUES (1,'Ebela','frankfurt','ebela@gmail.com'), (2,'Nija','Gotland','nija@gmail.com')
;

INSERT INTO lessons(lesson_id,teacher_id,lesson_date,lesson_time,instrument)
VALUES (1,1,'2026-10-01','12.40','Violin'), (2,1,'2026-11-01','12.30','Guitar')
;
INSERT INTO lessons(lesson_id,teacher_id,lesson_date,lesson_time,instrument)
VALUES (3,2,'2026-12-01','00.40','Piano'), (4,1,'2026-11-01','01.30','Piano')
;

INSERT INTO student_lessons(student_id,lesson_id,status)
VALUES (1,2,'NEW'),(1,3,'INPROGRESS'), (2,2,'COMPLETED'),(2,4,'NEW'),(1,4,'NEW')
;

SELECT * from students;
SELECT * FROM teachers;
SELECT * FROM lessons;

-- How many teacher taking Piano class
SELECT count(*) FROM lessons WHERE instrument='Piano';

-- Which teacher knows Piano
-- solution with JOIN
SELECT t.name
FROM teachers t
JOIN lessons l ON t.teacher_id = l.teacher_id
WHERE l.instrument = 'Piano'
;
-- other solution with sub query
SELECT t.name
FROM teachers t
WHERE EXISTS (SELECT 1 FROM lessons l WHERE t.teacher_id = l.teacher_id AND l.instrument = 'Piano')
;

SELECT t.name 
FROM teachers t
WHERE t.teacher_id IN (SELECT l.teacher_id FROM lessons l WHERE l.instrument = 'Piano')
;

-- Show all the teachers and the instrument they teach with session date
SELECT t.name , l.instrument, l.lesson_date
FROM teachers t
JOIN lessons l ON t.teacher_id = l.teacher_id
ORDER BY t.name,l.lesson_date,l.instrument
;

-- Which students attended Piano class on '2026-11-01'
SELECT DISTINCT s.name
FROM students s
JOIN student_lessons sl ON s.student_id = sl.student_id
JOIN lessons l ON sl.lesson_id = l.lesson_id
WHERE l.lesson_date = '2026-11-01'
;


-- summary of registered students in different lessons and status
SELECT s.name AS student,l.lesson_date,l.lesson_time,sl.status
FROM students s
JOIN student_lessons sl ON s.student_id = sl.student_id
JOIN lessons l ON sl.lesson_id = l.lesson_id
ORDER BY s.name
;

-- counts of COMPLETED, INPROGRESS and NEW sessions
SELECT status,COUNT(*) AS status_count 
FROM student_lessons
GROUP BY status;