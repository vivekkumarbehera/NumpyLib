list1=['VICKY','PYTHON','NUMPY','PANDAS']
list2=[i.lower() for i in list1]
print(list2)
list=["vicky","python","numpy","pandas"]
list3=[i.upper() for i in list]
print(list3)
for i in list1:
    print(i.upper())
    print(i.lower())
list=[]
for i in range(3):
    for j in range(3):
        list.append((i,j))
print(list)
list5=[(i,j) for i in range(3) for j in range(3)]
print(list5)