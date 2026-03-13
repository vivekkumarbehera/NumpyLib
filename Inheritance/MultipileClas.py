#Multipile Inheritance
class Parent1:
    def method1(self):
        print("This is a method in Parent1.")   
class Parent2:
    def method2(self):
        print("This is a method in Parent2.")
class Child2(Parent1, Parent2):
    def child_method(self):
        print("This is a method in the Child class.")
child_instance = Child2()
child_instance.method1()
child_instance.method2()
child_instance.child_method()
#Taking another example
class Father:
    def father_method(self):
        print("This is a method in the Father class.")
class Mother:
    def mother_method(self):
        print("This is a method in the Mother class.")
class Child(Father, Mother):
    def child_method(self):
        print("This is a method in the Child class.")
child_instance = Child()
child_instance.father_method()
child_instance.mother_method()
child_instance.child_method()
#One more example
class Teacher:
    def teacher_method(self):
        print("This is a method in the Teacher class.")
class Student:
    def student_method(self):
        print("This is a method in the Student class.")
class TeachingAssistant(Teacher, Student):
    def ta_method(self):
        print("This is a method in the Teaching Assistant class.")  
ta_instance = TeachingAssistant()
ta_instance.teacher_method()
ta_instance.student_method()
ta_instance.ta_method()
