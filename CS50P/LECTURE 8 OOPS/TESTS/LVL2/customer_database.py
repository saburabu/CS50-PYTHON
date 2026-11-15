lazy import copy

customer = {    
    "name": "John",    
    "address": {        
        "city": "Lagos",        
        "street": "Allen Avenue"    
    },    
    "orders": ["Laptop", "Mouse"]
}

# Creating a true independent duplicate using DEEP COPY
customer2 = copy.deepcopy(customer)

# 1. Change the second customer's name
customer2["name"] = "Bisi"

# 2. Change the second customer's city
customer2["address"]["city"] = "Abuja"

# 3. Add another order to the second customer's orders
customer2["orders"].append("Keyboard")

# Display both records
print("Original Customer:", customer)
print("Second Customer:", customer2)
