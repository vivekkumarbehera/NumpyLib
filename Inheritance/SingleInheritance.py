class Parent:
    def parent_method(self):
        print("This is a method in the Parent class.")
class Child(Parent):
    def child_method(self):
        print("This is a method in the Child class.")
child_instance = Child()
child_instance.parent_method()  
child_instance.child_method()  
