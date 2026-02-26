#Multilevel Inheritance using super() keyword
class Grandparent:
    def grandparent_method(self):
        print("This is a method in the Grandparent class.")
class Parent(Grandparent):
    def parent_method(self):
        print("This is a method in the Parent class.")
class Child(Parent):
    def child_method(self):
        print("This is a method in the Child class.")
        super().parent_method()  
        super().grandparent_method()
child_instance = Child()
child_instance.child_method()
