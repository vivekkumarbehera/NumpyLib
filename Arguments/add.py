s=lambda a,b:a+b
print(s(10,20))
d=lambda x:x*x
print(d(5))
l=[1,2,3,3,4,5]
s=list(map(lambda x:x*x,l))
print(s)
l=["Vivek","Vicky","Spidy"]
s=list(map(lambda x:x[0],l))
print(s)
l=["Vivek","Vicky","Spidy","Rahul","Subham","jarvis"]
s=list(filter(lambda x:x[0]=="V",l))
print(s)