#Update of the set, tuple, dictionary and list
#List operations
my_list = []
print(type(my_list))
print(my_list)
my_list.extend([1,2,3,4,5]) #Adding multiple elements to the list  
print(my_list)
my_list.append(6) #Adding a single element to the list
print(my_list)
list=[1,2,3,4,5]
print(list)
#Tuple operations
my_tuple = ()
print(type(my_tuple))
print(my_tuple)
my_tuple = (1, 2, 3, 4, 5) #Creating a tuple with multiple elements
print(my_tuple)
#Update of the set, tuple, dictionary and list
#Dictionary operations
my_dict = {}
print(type(my_dict))
print(my_dict)
my_dict["name"] = "Alice" #Adding a key-value pair to the dictionary
my_dict["age"] = 30
my_dict["city"] = "New York"
print(my_dict)
person = {"name": "Vivek", "age": 21}
person.update({"age": 22, "city": "Bhubaneshwar"})
print(person)
my_set = set(my_dict)
print(my_set)
