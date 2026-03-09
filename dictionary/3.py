orders = [
    {"item": "burger",  "price": 500},
    {"item": "pizza",   "price": 1200},
    {"item": "burger",  "price": 500},
    {"item": "fries",   "price": 200},
    {"item": "pizza",   "price": 1200},
    {"item": "burger",  "price": 500},
]

result = {}
for i in orders : # each dictionary 
    item = i["item"]
    result[item] = result.get(item,0) + 1
    # -- yahn apke pass hoga item or order number


top = max(result,key =result.get )

revenue = {}
for i in orders :
    item = i["item"]
    price = i["price"]

    revenue[item] = revenue.get(item,0) + price