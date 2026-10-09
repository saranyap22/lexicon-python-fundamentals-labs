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