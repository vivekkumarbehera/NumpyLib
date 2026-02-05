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

