text="  Hello my name is Vivek  "
print(text.upper())          # Convert to uppercase
print(text.lower())          # Convert to lowercase 
print(text.capitalize())     # Capitalize first letter
print(text.istitle())          # Title Case
print(text.title())          # Title Case
print(text.count("is"))     # Count occurrences of substring
print(text.find("Vivek"))  # Find substring index
print(text.startswith("He")) # Check starts with substring
print(text.endswith("Vivek  ")) # Check ends with substring
print(text.replace("Vivek", "Vicky")) # Replace substring
rollnp = "  12345  "
print(rollnp.strip())       # Remove leading/trailing whitespace
print(rollnp.isdigit())     # Check if all characters are digits
print(text.split())         # Split string into list
print("-".join(["2024", "06", "15"])) # Join list into string
list=['apple', 'banana', 'cherry']
g= "apple" in list 
print(g)
p="apple" not in list 
print(p)
marks=[85, 90, 78, 92, 88]
average = sum(marks) / len(marks)
print("Average marks:", average)
if average >= 90:
    print("Grade: A")
elif average >= 80:
    print("Grade: B")   
elif average >= 70:
    print("Grade: C")
elif average >= 60:
    print("Grade: D")
else:
    print("Grade: F")
if max(marks) > 95:
    print("Excellent performance!")
if min(marks) < 50:
    print("Needs improvement.") 

number = [3, 1, 4, 1, 5, 9, 2, 6, 5]
even_numbers = [num for num in number if num % 2 == 0]
print("Even numbers:", even_numbers)
#String Even or Odd 
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even") 
else:
    print(f"{num} is Odd")  