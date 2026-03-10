f=open("poem.txt","r")
print(f.readline())
print(f.readlines())
print(f.read())
f=open("poem.txt","a")
f.write("This is a new line added to the poem.")
f=open("poem.txt","w")
f.write("This will overwrite the existing content of the poem.")
#i want back
f=open("poem.txt","r")
print(f.read())


