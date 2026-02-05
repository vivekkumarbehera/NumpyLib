#Shoping Cart Dictionary
cart = {
    "items": [
        {"name": "Laptop", "price": 999.99, "quantity": 1},
        {"name": "Mouse", "price": 25.50, "quantity": 2},
        {"name": "Keyboard", "price": 45.00, "quantity": 1}
    ],
    "total": 0.0
}
#Operations on shopping cart
cart["items"].append({"name": "Tv", "price": 500.00, "quantity": 1})
print(cart)
#get operation
first_item = cart["items"][0]
print(first_item)
#update operation
cart["items"][1]["quantity"] = 3
print(cart)
#delete operation
del cart["items"][2]
print(cart)
#calculate total
total = sum(item["price"] * item["quantity"] for item in cart["items"])
cart["total"] = total
print(cart)
#values operation
total_value = cart["total"]
print(total_value)
#clear cart
cart["items"].clear()
cart["total"] = 0.0
print(cart)
#check if cart is empty
if not cart["items"]:
    print("The shopping cart is empty.")
else:
    print("The shopping cart has items.")

#For loop to iterate through items
for item in cart["items"]:
    print(f"Item: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")
#Check if an item is in the cart
item_name = "Laptop"
item_in_cart = any(item["name"] == item_name for item in cart["items"])
if item_in_cart:
    print(f"{item_name} is in the cart.")
else:
    print(f"{item_name} is not in the cart.")
#Get item details safely
item_details = next((item for item in cart["items"] if item["name"] == item_name), None)
if item_details:
    print(f"Details of {item_name}: {item_details}")    
else:
    print(f"{item_name} not found in the cart.")
#Set default for a new item
new_item = cart.setdefault("items", [])
print(new_item)
#Update cart with new item
cart.update({"items": [{"name": "Headphones", "price": 75.00, "quantity": 1}]})
print(cart)
cart["items"].pop()
print(cart)
cart["new_items"] = [{"name": "Monitor", "price": 150.00, "quantity": 1}]
print(cart)
cart.update({"name":"Office Supplies","date":"2024-06-15","status":"Pending"})
print(cart)