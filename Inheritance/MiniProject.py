class College:
    def __init__(self, college_name, **kwargs):
        super().__init__(**kwargs)
        self.college_name = college_name


class Student(College):
    def __init__(self, name, rollno, section, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.rollno = rollno
        self.section = section


class AcademicMark(Student):
    def __init__(self, marks, **kwargs):
        super().__init__(**kwargs)
        self.marks = marks


class SportsMark(Student):
    def __init__(self, sports_marks, **kwargs):
        super().__init__(**kwargs)
        self.sports_marks = sports_marks


class StudentReport(AcademicMark, SportsMark):
    def __init__(self, college_name, name, rollno, section, marks, sports_marks):
        super().__init__(
            college_name=college_name,
            name=name,
            rollno=rollno,
            section=section,
            marks=marks,
            sports_marks=sports_marks,
        )

    def display_report(self):
        print(f"College: {self.college_name}")
        print(f"Student Name: {self.name}")
        print(f"Roll No: {self.rollno}")
        print(f"Section: {self.section}")
        print(f"Academic Marks: {self.marks}")
        print(f"Sports Marks: {self.sports_marks}")


# Example usage
student_report = StudentReport("ABC College", "John Doe", "12345", "A", 85, 90)
student_report.display_report()
