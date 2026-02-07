class Student():
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
        
    def get_grades(self):
        return self.grades
    
class Course():
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def average_student(self):
        if not self.students:
            return 0
        
        total = sum(student.get_grades() for student in self.students)
        return total / len(self.students)

s1 = Student('Thabo', 32, 85)
s2 = Student('Chalatse', 19, 90)

course1 = Course('CompScience', 2)

course1.add_student(s1)
course1.add_student(s2)

print(course1.average_student())  

