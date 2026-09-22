""" Module to cretae Course Manager"""
# PART - F and PART - G


class Student:
    def __init__(self, name, score):
        self.name = name
        if self.validate_score(score):
            self.score = score

    def result(self):
        if self.score >= 60:
            return "Pass"

        return "Fail"

    def update_score(self, score):
        if self.validate_score(score):
            self.score = score

    def validate_score(self, score):
        if score < 0 or score > 100:
            raise ValueError("Score should be between zero and 100")
        return True


class Teacher:
    def __init__(self, name):
        self.name = name


class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def passed_students(self):
        return [student
                for student in self.students
                if student.result() == "Pass"]

    def course_summary(self):
        print(f"{"Course Name": <5}: {self.name:<5}")
        print(f"{"Teacher Name":<5}: {self.teacher.name:<5}\n")
        print("Students: ")
        for student in self.students:
            print(f"{student.name:<20} {"-":<3} {student.score:<5}")
        print(f"\n{"Number of Students":<5} : {self.student_count():<5}\n")
        print("Passed Students: ")
        for student in self.passed_students():
            print(f"{student.name:<20} {"-":<3} {student.score:<5}")

    def student_count(self):
        return len(self.students)

    def add_student(self, student):
        self.students.append(student)

    def student_above_threshold(self, threshold_score):
        return [
            student
            for student in self.students
            if student.score >= threshold_score
        ]


# Creating course object
course = Course(
    "Python Fundamentals",
    Teacher("Sara")
)

course.add_student(Student("Aana", 67))
course.add_student(Student("Bob", 10))
course.add_student(Student("Richard", 50))

course.course_summary()

# -------------------
# creating new course object

course2 = Course(
    "Java Fundamentals",
    Teacher("Menu")
)

course2.add_student(Student("Helen", 79))
course2.add_student(Student("Emma", 80))
course2.add_student(Student("Kick", 55))

course2.course_summary()

course2.add_student(Student("Kick", 550))
