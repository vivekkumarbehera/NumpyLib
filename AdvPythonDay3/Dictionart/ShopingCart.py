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
