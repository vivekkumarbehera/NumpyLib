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
#write the poem again
f=open("poem.txt","w")
f.write("Roses are red,\nViolets are blue,\nSugar is sweet,\nAnd so are you.")
f=open("poem.txt","r")
#Append a new line to the poem
f=open("poem.txt","a")
f.write("\nThis is an additional line to the poem.")
f=open("poem.txt","r")
print(f.read())
f.close()


