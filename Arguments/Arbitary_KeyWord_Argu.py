#Arbitary_KeyWord Arguments
def Stu(name,age,rollno,section):
    print(f"Hello Good Morning !! My name is {name} ")
Stu(name='Aniket',age=22,rollno=101,section='I')
Stu(rollno=101,section='I',name='vivek',age=22)
def str (info):
    print("Name of the Student",info['name'])
    print("Blood group of the Student is ",info["Blood Group"])
    print(len(info))
    print(type(info))
info={"Name":"Vivek","age":21,"BloodGroup":"O+","City":"Mnglore"}
str(info)
def emp(**info):
    print("Name of the Student:", info['name'])
    print("Blood group of the Student is:", info['Bloodgroup'])
    print("Number of items in info:", len(info))
    print("Type of info:", type(info))

emp(name="vivek", Bloodgroup="O+")