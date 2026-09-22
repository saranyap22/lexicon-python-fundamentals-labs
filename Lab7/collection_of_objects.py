class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self):
        if self.score >= 70:
            return "Pass"
        return "Fail"

    def score_above_threshold(self, threshold):
        if self.score >= threshold:
            return True
        return False


students = [
    Student("sara", 56),
    Student("Emma", 90),
    Student("Helen", 34),
    Student("Victor", 12),
    Student("Tintu", 0),
    Student("Ibrahim", 100)
]

for student in students:
    print(f"{student.name:<15} : {student.score}")

for student in students:
    print(f"{student.name:<15} : {student.get_status()}")

passed_students = [
    student
    for student in students
    if student.score_above_threshold(70)
]

print("Passed Students:", passed_students)

# ----------------------------------

# Objects inside Objects


class Teacher:
    def __init__(self, name):
        self.name = name


class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)


teacher = Teacher("Yamuna")
course = Course("Python Fundamentals", teacher)
print(f"Course Name: {course.name}  Teacher Name: {teacher.name}")

course.add_student(Student("Lima", 80))
course.add_student(Student("Hemanth", 0))
course.add_student(Student("Geneeth", 70))

for student in course.students:
    print(student.name)
