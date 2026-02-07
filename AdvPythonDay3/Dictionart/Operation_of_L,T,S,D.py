#Update of the set, tuple, dictionary and list
#List operations
my_list = []
print(type(my_list))
print(my_list)
my_list.extend([1,2,3,4,5]) #Adding multiple elements to the list  
print(my_list)
my_list.append(6) #Adding a single element to the list
print(my_list)

#Set operations
my_set = set()
print(type(my_set))
print(my_set)
my_set.update([1, 2, 3, 4, 5]) #Adding multiple elements to the set
print(my_set)

#Removing an element from the set
my_set.remove(3)
print(my_set)

#Discard an element from the set
my_set.discard(4)
print(my_set)