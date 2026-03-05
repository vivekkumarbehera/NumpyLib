print(__name__)
""" this is the documentation string of the model.py file"""
print(__doc__)# this is the documentation string of the model.py file
print(__file__)# this is the file name of the model.py file
class MyClass:
    def __init__(self, name):
        self.name = name
m = MyClass("Alice")
print(m.name)

print(m.__dict__) # this is the dictionary of the m object of the MyClass class
print(MyClass.__doc__)# this is the documentation string of the MyClass class
print(MyClass.__name__)# this is the name of the MyClass class  
print(MyClass.__module__)# this is the module name of the MyClass class]
print(MyClass.__dict__)# this is the dictionary of the MyClass class


x= 10
print(x.__class__)# this is the class of the x variable
print(x.__doc__)# this is the documentation string of the x variable