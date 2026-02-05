person =  {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person["name"])  # Accessing value by key
person["age"] = 31  # Modifying value
print(person)
#Constructor to create a dictionary
dict2 = dict(name="Alice", age=25, city="Los Angeles")
print(dict2)
person={'name': 'Alice', 'age': 25, 'marks':{80,60,90}}
person_keys=person.keys()
print(person_keys)
person_values=person.values()
print(person_values)
#Book dictionary
book = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925,
    "genres": ["Novel", "Historical"],
    "available": True
}
print(book["title"])  # Accessing title
print(book["author"])  # Accessing author
print(book["year"])  # Accessing year
print(book["genres"])  # Accessing genres
print(book["available"])  # Accessing availability
#Book diffrerent operations
book["publisher"] = "Scribner"  # Adding a new key-value pair
print(book)
book["available"] = False  # Modifying existing value
print(book)
del book["year"]  # Deleting a key-value pair
print(book)
for key, value in book.items():
    print(f"{key}: {value}")  # Iterating through dictionary
#Checking if a key exists
if "author" in book:
    print("Author is present in the book dictionary.")  
else:

    print("Author is not present in the book dictionary.")

if "year" not in book:
    print("Year is not present in the book dictionary.")    
else:
    print("Year is present in the book dictionary.")
x=book.get("title")
print(x)
y=book.get("year","Not Found")
print(y)
z=book.setdefault("year", 1925)
print(z)
print(book)
book.pop("available")
print(book)
book.items()
print(book)
book.update({"year": 1926})
print(book)
book.update({"pages": 180})
print(book)