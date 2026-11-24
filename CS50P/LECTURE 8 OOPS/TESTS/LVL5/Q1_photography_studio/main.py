import re

class EquipmentItem:
    VALID_CATEGORIES = [
        "camera", "lens", "lighting", "accessory", "tripod", "backdrop",
        "modifier", "audio", "storage", "power", "tethering", "gimbal",
        "drone", "grip"
    ]

    def __init__(self, name, serial_number, category, purchase_price):
        if not isinstance(name, str) or not name.strip():
            raise ValueError(f"Name of equipment can't be '{name}'; it must be a string.")

        if not isinstance(category, str) or category.strip().lower() not in self.VALID_CATEGORIES:
            raise ValueError(
                f"Invalid category '{category}'. Must be one of: {', '.join(sorted(self.VALID_CATEGORIES))}."
            )

        self.name = name.strip()
        self.category = category.strip().lower()
        self.serial_number = serial_number
        self.purchase_price = purchase_price

    @property
    def serial_number(self):
        return self._serial_number

    @serial_number.setter
    def serial_number(self, value):
        if not isinstance(value, str) or not re.fullmatch(r"STUDIO_EQUIP_\d{4}_[a-z]{4}", value):
            raise ValueError("Serial number does not meet the required format.")
        self._serial_number = value

    @property
    def purchase_price(self):
        return self._purchase_price

    @purchase_price.setter
    def purchase_price(self, value):
        if isinstance(value, bool) or not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Purchase price must be a positive number.")
        self._purchase_price = float(value)

    def __str__(self):
        return f"Name: {self.name}, Serial: {self.serial_number}, Category: {self.category}, Price: {self.purchase_price}"

    def __repr__(self):
        return f"EquipmentItem('{self.name}', '{self.serial_number}')"


class Equipment:
    def __init__(self):
        self._equipments = []

    def _validate_serial_format(self, serial_number):
        if not isinstance(serial_number, str) or not re.fullmatch(r"STUDIO_EQUIP_\d{4}_[a-z]{4}", serial_number):
            raise ValueError("Invalid serial number format.")

    def add_equipment(self, equipment):
        if not isinstance(equipment, EquipmentItem):
            raise TypeError("Expected an EquipmentItem instance.")

        for existing in self._equipments:
            if existing.serial_number == equipment.serial_number:
                raise ValueError(
                    f"Equipment with this serial number already exists: {existing.name}"
                )

        self._equipments.append(equipment)

    def remove_equipment(self, serial_number):
        self._validate_serial_format(serial_number)

        for index, item in enumerate(self._equipments):
            if item.serial_number == serial_number:
                removed = self._equipments.pop(index)
                return f"{removed.name} has been removed. Remaining items: {len(self._equipments)}"

        raise ValueError("Serial number doesn't exist in the database.")

    def find_equipment(self, serial_number):
        self._validate_serial_format(serial_number)

        for item in self._equipments:
            if item.serial_number == serial_number:
                return f"Name: {item.name}, Serial number: {item.serial_number}\nCategory: {item.category}, Purchase price: {item.purchase_price}"

        raise ValueError("Serial number doesn't exist in the database.")

    def total_price(self):
        total = sum(x.purchase_price for x in self._equipments)
        return f"Total price: {total}", total

    def __str__(self):
        if not self._equipments:
            return "No equipment in inventory."
        return "\n".join(str(item) for item in self._equipments)


# --- Testing ---
item0 = EquipmentItem("Camera", "STUDIO_EQUIP_1234_hiwd", "camera", 30000)
item1 = EquipmentItem("Lens", "STUDIO_EQUIP_1234_lens", "lens", 15000)
item2 = EquipmentItem("Lighting Kit", "STUDIO_EQUIP_1234_ligh", "lighting", 20000)
item3 = EquipmentItem("Tripod", "STUDIO_EQUIP_1234_trip", "tripod", 5000)
item4 = EquipmentItem("Backdrop", "STUDIO_EQUIP_1234_back", "backdrop", 8000)
item5 = EquipmentItem("Audio Recorder", "STUDIO_EQUIP_1234_audi", "audio", 12000)

hi = Equipment()
for item in [item0, item1, item2, item3, item4, item5]:
    hi.add_equipment(item)

print("--- Find ---")
print(hi.find_equipment("STUDIO_EQUIP_1234_hiwd"))

print("\n--- All Equipment ---")
print(hi)
print(hi.total_price()[0])

print("\n--- Removing ---")
print(hi.remove_equipment("STUDIO_EQUIP_1234_hiwd"))
print(hi.remove_equipment("STUDIO_EQUIP_1234_lens"))
print(hi.remove_equipment("STUDIO_EQUIP_1234_ligh"))  
print(hi.remove_equipment("STUDIO_EQUIP_1234_trip"))

print("\n--- Remaining Equipment ---")
print(hi)
print(hi.total_price()[0])

input("name")
