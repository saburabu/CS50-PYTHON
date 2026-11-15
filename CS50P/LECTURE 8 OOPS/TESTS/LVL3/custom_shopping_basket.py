import re

class Products:
    @staticmethod
    def validate_dict(product_dict):
        # 1. Check that it's a non-empty dictionary
        if not isinstance(product_dict, dict) or not product_dict:
            return False

        # 2. Safely extract keys (chaining .get() instead of using 'or' inside the string)
        product_id = product_dict.get("product_id") or product_dict.get("id")
        product_name = product_dict.get("product_name") or product_dict.get("name")
        unit_price = (
            product_dict.get("unit_price") 
            if product_dict.get("unit_price") is not None 
            else product_dict.get("price") or product_dict.get("product_price")
        )
        quantity = (
            product_dict.get("quantity") 
            if product_dict.get("quantity") is not None 
            else product_dict.get("product_quantity")
        )

        # 3. Check string types and ensure they aren't empty/blank
        if not all(isinstance(x, str) and x.strip() for x in [product_id, product_name]):
            return False

        # 4. Check number types (explicitly excluding booleans!)
        if not all(isinstance(y, (int, float)) and not isinstance(y, bool) for y in [unit_price, quantity]):
            return False

        # 5. Check business logic (regex format & non-negative values)
        if not re.fullmatch(r"^PROD-\d{4}$", product_id):
            return False
            
        if unit_price <= 0 or quantity < 0:
            return False

        return True

    def __init__(self, product_dict):
        if self.validate_dict(product_dict):
            product_id = product_dict.get("product_id") or product_dict.get("id")
            product_name = product_dict.get("product_name") or product_dict.get("name")
            unit_price = (
                product_dict.get("unit_price") 
                if product_dict.get("unit_price") is not None 
                else product_dict.get("price") or product_dict.get("product_price")
            )
            quantity = (
                product_dict.get("quantity") 
                if product_dict.get("quantity") is not None 
                else product_dict.get("product_quantity")
            )

            self.id = product_id
            self.name = product_name
            self.price = unit_price
            self.quantity = quantity
        else:
            raise ValueError("Enter the proposed types and values and organise the keys properly and it must be a dict")


class ShoppingBasket:
    def __init__(self):
        self.products = {Products}

# abandoned project


