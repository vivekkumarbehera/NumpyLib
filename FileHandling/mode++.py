#we are using the  r++, w++ and a++ modes to read, write and append to the file respectively.
#r++ mode is used to read and write
with open("poem2.txt","r+") as f:
    content = f.read()
    print(content)
    f.write("\nThis is a new line added to the poem using r++ mode.")
with open("poem2.txt","a+") as f:
    f.write("\nThis is a new line added to the poem using a++ mode.")
    content = f.read()
    print(content)
f=open("poem2.txt","r+")
print(f.tell())# this will print the current position of the file pointer
f.write("\nThis is a new line added to the poem using r++ mode.")
print(f.tell())
print(f.seek(0))# this will move the file pointer to the beginning of the file
print(f.read())

#a++ mode read and append
with open("poem2.txt","a+") as f:
    f.write("\nThis is a new line added to the poem using a++ mode.")
    f.seek(0)
    content = f.read()
    print(content)
    f.seek(0)
    print(f.read())
f=open("poem2.txt","a+")
print(f.tell())# this will print the current position of the file pointer   
f.write("\nThis is a new line added to the poem using a++ mode.")
print(f.tell())
print(f.seek(0))# this will move the file pointer to the beginning of the file
print(f.read())
#w++ mode is used to write and read
with open("poem2.txt","w+") as f:
    f.write("This will overwrite the existing content of the poem using w++ mode.")
    f.seek(0)
    content = f.read()
    print(content)
    f.seek(0)
    print(f.read())
    f.write("\nThis is a new line added to the poem using w++ mode.")   
with open("poem2.txt","r") as f:
    print(f.read())
    f.seek(0)
    print(f.read())
                    