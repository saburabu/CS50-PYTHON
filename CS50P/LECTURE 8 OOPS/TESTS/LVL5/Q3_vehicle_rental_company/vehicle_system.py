from models import Customer, Vehicle, Mechanic, VEHICLES_FILE
import pathlib, json


class ManagementSystem:
    directory = pathlib.Path(__file__).resolve().parent
    sales_file = directory / "sales.json"

    @staticmethod
    def _load_json(file_path: pathlib.Path) -> list:
        if file_path.exists() and file_path.stat().st_size > 0:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        return []

    @staticmethod
    def _save_json(file_path: pathlib.Path, data: list):
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def save_sales(vehicle_plate_number, vehicle_name, buyer_name, buyer_nin, buyer_phone_number):
        sales = ManagementSystem._load_json(ManagementSystem.sales_file)

        sales.append({
            "vehicle_plate_number": vehicle_plate_number,
            "vehicle_name": vehicle_name,
            "buyer_name": buyer_name,
            "buyer_nin": buyer_nin,
            "buyer_phone_number": buyer_phone_number
        })

        ManagementSystem._save_json(ManagementSystem.sales_file, sales)

    def register_vehicle(self, vehicle: Vehicle):
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Vehicle must be an object of the Vehicle class")

        vehicle.save_vehicle()

    def sell_vehicle(self, customer: Customer, vehicle: Vehicle, amount: float):
        if not isinstance(customer, Customer) or not isinstance(vehicle, Vehicle):
            raise TypeError("Customer and vehicle must be instances of Customer and Vehicle")

        # 1. Load vehicles.json and look for the vehicle by plate number
        vehicles_inventory = self._load_json(VEHICLES_FILE)
        matched_record = next(
            (item for item in vehicles_inventory if item.get("plate_number") == vehicle.plate_number),
            None
        )

        # 2. Validate existence, condition, and amount
        if matched_record is None:
            raise ValueError(f"Vehicle with plate number '{vehicle.plate_number}' not found in inventory.")

        if matched_record.get("condition") != "Good":
            raise ValueError(f"Cannot sell vehicle: condition is '{matched_record.get('condition')}', must be 'Good'.")

        if amount != matched_record.get("price"):
            raise ValueError(f"Invalid Amount: expected {matched_record.get('price')}, got {amount}.")

        # 3. Decrement quantity or remove from vehicles.json if quantity reaches 0
        if matched_record.get("quantity", 1) > 1:
            matched_record["quantity"] -= 1
            updated_inventory = vehicles_inventory
        else:
            updated_inventory = [
                item for item in vehicles_inventory
                if item.get("plate_number") != vehicle.plate_number
            ]

        self._save_json(VEHICLES_FILE, updated_inventory)

        # 4. Record the sale in sales.json and assign vehicle to the customer
        vehicle_full_name = f"{vehicle.make} {vehicle.model}"
        self.save_sales(
            vehicle.plate_number,
            vehicle_full_name,
            customer.name,
            customer.nin,
            customer.phone
        )
        customer.add_vehicle(vehicle)
