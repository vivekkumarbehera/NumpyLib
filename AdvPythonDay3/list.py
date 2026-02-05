#List
list1 = [1, 2, 3, 4, 5]
print("Original List:", list1)
#Appending an element
list1.append(6)
print("After Appending 6:", list1)
#Removing an element
list1.remove(3)
print("After Removing 3:", list1)
#Accessing elements
print("Element at index 2:", list1[2])  
#Slicing the list
print("Sliced List (index 1 to 4):", list1[1:4])
#Iterating through the list
for item in list1:
    print("List Item:", item)   
#Length of the list
print("Length of List:", len(list1))
#Sorting the list
list1.sort(reverse=True)
print("Sorted List in Descending Order:", list1)
#Finding the index of an element
index_of_4 = list1.index(4)
print("Index of element 4:", index_of_4)
#extending the list
list2 = [7, 8, 9]
list1.extend(list2)
print("After Extending with [7, 8, 9]:", list1)
#reversing the list
list1.reverse() 
print("Reversed List:", list1)
#inserting an element at a specific position
list1.insert(2, 10) 
print("After Inserting 10 at index 2:", list1)
#counting occurrences of an element
count_of_2 = list1.count(2) 
print("Count of element 2:", count_of_2)
#popping an element
popped_element = list1.pop()
print("Popped Element:", popped_element)
print("List after Popping an element:", list1)
#clearing the list
list1.clear()   
print("List after Clearing:", list1)
#copying a new list with range
list3 = list(range(1, 11))
print("New List with range 1 to 10:", list3)
list4 = list3.copy()
print("Copied List:", list4)
#List Summation
list1 = [1, 2, 3, 4, 5]
total = sum(list1)
print("Sum of elements in List1:", total)    
#even numbers from a list
numbers = [10, 15, 20, 25, 30, 35]
even_numbers = [num for num in numbers if num % 2 == 0]     
print("Even numbers from the list:", even_numbers)
#finding maximum and minimum
list5 = [5, 3, 8, 6, 2]
print(list5)
largest_value=list5[0]
for list in list5:
    if list>largest_value:
        largest_value=list
print("Largest value in List5:", largest_value)
smallest_value=list5[0]
for list in list5:
    if list<smallest_value:
        smallest_value=list 
print("Smallest value in List5:", smallest_value)
#Membership testing
fruits = ['apple', 'banana', 'cherry']
is_apple_present = 'apple' in fruits
print("Is 'apple' present in fruits list?", is_apple_present)
is_mango_absent = 'mango'  in fruits
print("Is 'mango' absent in fruits list?",  is_mango_absent)
#Starting and ending variables
numbers = [10, 20, 30, 40, 50]
for num in numbers:
    if str(num).startswith('1'):
        print(f"{num} starts with 1")
    if str(num).endswith('0'):
        print(f"{num} ends with 0")
#Match expression
day = input("Enter a day number (1-7): ")
match day:
    case '1':
        print("It's Monday, the start of the week!")
    case '2':
        print("It is the tuesday")
    case '3':
        print("It is the wednesday")
    case '4':
        print("It is the thursday") 
    case '5':
        print("It is the friday")
    case '6':
        print("It is the saturday") 
    case '7':
        print("It is the sunday")
    case _:
        print("Invalid day! Please enter a number between 1 and 7.")   
#Match Expression with calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
match operation:
    case '+':
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}.")
    case '-':
        result = num1 - num2
        print(f"The difference between {num1} and {num2} is {result}.")
    case '*':
        result = num1 * num2
        print(f"The product of {num1} and {num2} is {result}.")
    case '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The division of {num1} by {num2} is {result}.")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation. Please enter one of +, -, *, /.")