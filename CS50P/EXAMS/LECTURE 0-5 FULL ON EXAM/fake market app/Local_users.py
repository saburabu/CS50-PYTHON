from faker import Faker
import random
import json

fake = Faker()

def create_user_profile():
    profile = {
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address(),
        "account_number": fake.bban(),  # fake bank account number
        "balance": round(random.uniform(10.0, 100000.0), 2)  # random balance
    }
    return profile

user = create_user_profile()

print(user)

def create_products(num_products=300):
    products = []
    for _ in range(num_products):
        product = {
            "id": _ + 1,  # simple incremental ID
            "name": fake.word().capitalize(),
            "category": fake.word().capitalize(),
            "price": round(random.uniform(1.0, 1000.0), 2),
            "stock": random.randint(1, 100)
        }
        products.append(product)
    return products

products = create_products()

print(products)

with open("products.json", "w") as file:
    json.dump(products, file, indent=4)