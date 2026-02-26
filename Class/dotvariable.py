#dot variable in the class
class MyClass:
    def __init__(self, name):
        self.name = name
    def display_name(self):
        print("Name:", self.name)
m=MyClass("Alice")
m.display_name()       