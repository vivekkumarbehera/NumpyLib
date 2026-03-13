#Herarchical inheritance
class Parent:
    def parent_method(self):
        print("This is a method in the Parent class.")
class Child1(Parent):
    def child1_method(self):
        print("This is a method in the Child1 class.")
class Child2(Parent):
    def child2_method(self):
        print("This is a method in the Child2 class.")
child1_instance = Child1()
child1_instance.parent_method()
child1_instance.child1_method()
child2_instance = Child2()
child2_instance.parent_method()
child2_instance.child2_method()


