#Union
a= set((1,2,3,4,5))
b= set((4,5,6,7,8)) 
c= set((1,2,3))
print(a.union(b)) #Union of two sets
d= c | b #Union of two sets using operator  
print(d)


#Intersection
a= set((1,2,3,4,5))
b= set((4,5,6,7,8)) 
c= set((1,2,3))
print(a.intersection(b)) #Intersection of two sets
e= c & b #Intersection of two sets using operator   
print(e)

#Difference
a= set((1,2,3,4,5))
b= set((4,5,6,7,8)) 
c= set((1,2,3))
print(a.difference(b)) #Difference of two sets
f=  a-c #Difference of two sets using operator
print(f)
#Symmetric Difference
a= set((1,2,3,4,5))
b= set((4,5,6,7,8)) 
c= set((1,2,3))
print(a.symmetric_difference(c)) #Symmetric difference of two sets
g= a ^ b #Symmetric difference of two sets using operator
print(g)


