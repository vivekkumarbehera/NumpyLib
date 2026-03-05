class stu:
    def __init__(self,name,age):
        self.name = name
        self._age = age
        self.__rollno = 12345
    
    def get_rollno(self):
        return self.__rollno
s = stu("Alice", 20)
print(s.name) # this is the public variable of the stu class
print(s._age) # this is the protected variable of the stu class
print(s.get_rollno()) # this is the private variable of the stu class