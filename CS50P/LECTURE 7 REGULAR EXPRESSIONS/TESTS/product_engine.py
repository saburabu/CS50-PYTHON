lazy import re
users_search = input("Search here: ")

products = [
    "Samsung Galaxy S25",
    "Apple iPhone 17",
    "Samsung Galaxy A56",
    "HP EliteBook 840",
    "Apple MacBook Air",
    "Dell Latitude 7490"
]
results = [] 

if products and isinstance(products, list) and isinstance(users_search, str):
    search = re.escape(users_search)
    for product in products:
        if match := re.search(search, product, re.IGNORECASE):
            results.append(product)
        else:
            pass

if results:
    if len(results) > 1:
        # Number each product cleanly:
        numbered_results = [f"{i}. {product}" for i, product in enumerate(results, start=1)]
        result = "\n".join(numbered_results)
    else:
        # Just 1 product found, no numbering added
        result = results[0]
        
    print("Matched products:\n" + result)
else:
    print("An error occurred / No products matched")
