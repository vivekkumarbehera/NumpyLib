#StudentClass User Input
class Student:  
    def __init__(self, name, roll_number, section, city):  
        self.name = name   
        self.roll_number = roll_number  
        self.section = section
        self.city = city
    def display(self):  
        print("Name:", self.name)  
        print("Roll Number:", self.roll_number)
        print("Section:", self.section)
        print("City:", self.city)
name = input("Enter student's name: ")
roll_number = input("Enter student's roll number: ")
section = input("Enter student's section: ")
city = input("Enter student's city: ")
student = Student(name, roll_number, section, city)
student.display()