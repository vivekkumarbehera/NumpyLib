# college is the main class and student has name, rollno, section
class College:
    def __init__(self, name):
        self.name = name


class Student(College):
    def __init__(self, name, rollno, section):
        self.name = name
        self.rollno = rollno
        self.section = section


class AcademicMark(Student):
    def __init__(self, name, rollno, section, marks):
        # Use direct Student init to avoid MRO conflict in multiple inheritance.
        Student.__init__(self, name, rollno, section)
        self.marks = marks


class SportsMark(Student):
    def __init__(self, name, rollno, section, sports_marks):
        # Use direct Student init to avoid MRO conflict in multiple inheritance.
        Student.__init__(self, name, rollno, section)
        self.sports_marks = sports_marks


class StudentReport(AcademicMark, SportsMark):
    def __init__(self, name, rollno, section, marks, sports_marks):
        AcademicMark.__init__(self, name, rollno, section, marks)
        SportsMark.__init__(self, name, rollno, section, sports_marks)

    def display_report(self):
        print(f"Student Name: {self.name}")
        print(f"Roll No: {self.rollno}")
        print(f"Section: {self.section}")
        print(f"Academic Marks: {self.marks}")
        print(f"Sports Marks: {self.sports_marks}")


student_report = StudentReport("John Doe", "12345", "A", 85, 90)
student_report.display_report()
