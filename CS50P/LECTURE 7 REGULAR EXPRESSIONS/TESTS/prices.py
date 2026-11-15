lazy import re

products = """
Laptop: ₦850000
Mouse: ₦15000
Keyboard: ₦25000
Monitor: ₦320000
"""

if isinstance(products, str):
    if product := re.findall(r"\d+", products):
        print(product)