#f=open("poem2.txt","x")
with open("poem2.txt","r") as f:
    content = f.read()
with open("poem2.txt","w") as f:
    f.write("Roses are red,\nViolets are blue,\nSugar is sweet,\nAnd so are you.")
with open("poem2.txt","r") as f:
    print(f.read())
with open("poem2.txt","a") as f:
    f.write("\nThis is an additional line to the poem.")
with open("poem2.txt","r") as f:
    print(f.read())
