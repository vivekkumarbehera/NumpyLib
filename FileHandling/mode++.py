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
print(f.tell())
f.write("\nThis is a new line added to the poem using r++ mode.")
print(f.tell())
print(f.seek(0))
print(f.read())

