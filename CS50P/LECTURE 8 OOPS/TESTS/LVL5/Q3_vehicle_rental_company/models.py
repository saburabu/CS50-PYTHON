import json
import re
from datetime import datetime
import httpx
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
VEHICLES_FILE = BASE_DIR / "vehicles.json"
REPORTS_FILE = BASE_DIR / "reports.json"


class Vehicle:
    VEHICLE_TYPES = {
        "sedan", "suv", "hatchback", "bus", "van",
        "motorcycle", "tricycle", "coupe", "sports car", "race car"
    }
    vehicles = []

    @staticmethod
    def is_valid_make_model(make: str, model: str) -> bool:
        clean_make = make.strip()
        base = "https://" + "vpic.nhtsa.dot.gov"
        path = f"/api/vehicles/getmodelsformake/{clean_make}?format=json"
        url = base + path

        try:
            res = httpx.get(url, follow_redirects=True, timeout=5.0)
            res.raise_for_status()
        except httpx.HTTPError:
            return False

        results = res.json().get("Results", [])
        valid_models = {item["Model_Name"].strip().lower() for item in results}
        return model.strip().lower() in valid_models

    @staticmethod
    def is_valid_color_api(color: str) -> bool:
        clean_color = color.strip().lower()
        base = "https://" + "api.color.pizza"
        path = f"/v1/names/?name={clean_color}"
        url = base + path

        try:
            res = httpx.get(url, follow_redirects=True, timeout=5.0)
            res.raise_for_status()
        except httpx.HTTPError:
            return False

        colors = res.json().get("colors", [])
        return any(item.get("name", "").strip().lower() == clean_color for item in colors)

    def __init__(
        self,
        plate_number: str,
        make: str,
        model: str,
        year: int,
        color: str,
        vin: str,
        vehicle_type: str,
        quantity: int,
        price: float,
        owner_nin: str = None,
    ):
        if not isinstance(plate_number, str) or not re.fullmatch(r"[A-Z]{3}-?\d{3}[A-Z]{2}", plate_number.strip().upper()):
            raise ValueError("Invalid car plate number")

        if not isinstance(make, str) or not isinstance(model, str) or not self.is_valid_make_model(make, model):
            raise ValueError("The car model or make is invalid or both")

        if isinstance(year, bool) or not isinstance(year, int) or not (1900 <= year <= 2027):
            raise ValueError("Invalid year: year must be a 4-digit integer")

        if not isinstance(color, str) or not self.is_valid_color_api(color):
            raise ValueError("Invalid colour")

        if not isinstance(vin, str) or not re.fullmatch(r"[A-HJ-NPR-Z0-9]{17}", vin.strip().upper()):
            raise ValueError("Invalid VIN")

        if not isinstance(vehicle_type, str) or vehicle_type.strip().lower() not in self.VEHICLE_TYPES:
            raise ValueError(f"Invalid vehicle type. Must be one of: {', '.join(self.VEHICLE_TYPES)}")

        if owner_nin is not None and (not isinstance(owner_nin, str) or not re.fullmatch(r"\d{11}", owner_nin.strip())):
            raise ValueError("Invalid NIN: must be an 11-digit string")

        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            raise ValueError(f"Invalid quantity: {quantity}")

        if not isinstance(price, (float, int)) or isinstance(price, bool) or price < 200000:
            raise ValueError("Price must be greater than 200,000 naira and must be a float or int")

        self.plate_number = plate_number.strip().upper()
        self.make = make.strip().title()
        self.model = model.strip().title()
        self.year = year
        self.color = color.strip().lower()
        self.vin = vin.strip().upper()
        self.vehicle_type = vehicle_type.strip().lower()
        self.owner_nin = owner_nin.strip() if owner_nin else None
        self.condition = "Good"
        self.quantity = quantity
        self.price = price

    def save_vehicle(self):
        # 1. Read existing vehicles from vehicles.json
        if VEHICLES_FILE.exists() and VEHICLES_FILE.stat().st_size > 0:
            with open(VEHICLES_FILE, "r", encoding="utf-8") as file:
                existing_vehicles = json.load(file)
        else:
            existing_vehicles = []

        # 2. Append the new vehicle dictionary
        new_vehicle = {
            "plate_number": self.plate_number,
            "make": self.make,
            "model": self.model,
            "quantity": self.quantity,
            "price": self.price,
            "year": self.year,
            "color": self.color,
            "vin": self.vin,
            "vehicle_type": self.vehicle_type,
            "owner_nin": self.owner_nin,
            "condition": self.condition,
        }
        existing_vehicles.append(new_vehicle)
        Vehicle.vehicles = existing_vehicles

        # 3. Write the updated list back to vehicles.json
        with open(VEHICLES_FILE, "w", encoding="utf-8") as file:
            json.dump(existing_vehicles, file, indent=4)


class Customer:
    def __init__(self, name: str, DLN: str, NIN: str, phone_number):
        if not isinstance(name, str) or not re.fullmatch(r"[A-Za-z]+(?:\s[A-Za-z]+){1,2}", name.strip()):
            raise ValueError("Invalid Name")
        if not isinstance(DLN, str) or not re.fullmatch(r"[A-Za-z]{3}\d{5}[A-Za-z]{2}\d{2}", DLN.strip()):
            raise ValueError("Invalid driver license number")
        if not isinstance(NIN, str) or not re.fullmatch(r"\d{11}", NIN.strip()):
            raise ValueError("Invalid national identification number")
        if not isinstance(phone_number, str) or not re.fullmatch(r"\+234[0-9]{10}", phone_number):
            raise ValueError("Invalid phone number phone number pattern must be like e.g\"+234805153777\"")

        self.name = name.strip().title()
        self.dln = DLN.strip().upper()
        self.nin = NIN.strip()
        self.phone = phone_number
        self.vehicles = []

    def add_vehicle(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise ValueError("Vehicle must be from the Vehicle class")

        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise ValueError("Vehicle must be from the Vehicle class")

        for index, x in enumerate(self.vehicles):
            if x.plate_number == vehicle.plate_number:
                self.vehicles.pop(index)
                return

        raise ValueError("Vehicle plate number doesnt exist in inventory")


class Mechanic:
    VALID_CONDITIONS = {"Good", "Needs Maintenance", "Damaged", "Out of Service"}
    reports = []

    def __init__(self, name: str, worker_id: str):
        if not isinstance(name, str) or not re.fullmatch(r"[A-Za-z]+(?:\s[A-Za-z]+){1,2}", name.strip()):
            raise ValueError("Invalid Name")

        if not isinstance(worker_id, str) or not re.fullmatch(r"MECH-\d{3}", worker_id.strip().upper()):
            raise ValueError("Invalid id")

        self.name = name.strip().title()
        self.id = worker_id.strip().upper()
        self.vehicles = []

    def assign_vehicle(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise ValueError("Vehicle must be an object of the Vehicle class")

        if vehicle not in self.vehicles:
            self.vehicles.append(vehicle)

    def make_report(self, vehicle, condition: str) -> dict:
        if not isinstance(vehicle, Vehicle):
            raise ValueError("Vehicle must be an object of the Vehicle class")

        if vehicle not in self.vehicles:
            raise ValueError("Vehicle must be assigned to this mechanic before making a report")

        if not isinstance(condition, str) or condition not in self.VALID_CONDITIONS:
            raise ValueError(f"Invalid condition. Must be one of: {', '.join(self.VALID_CONDITIONS)}")

        # 1. Update the object in memory
        vehicle.condition = condition

        # 2. Sync the updated condition to vehicles.json if the car exists there
        if VEHICLES_FILE.exists() and VEHICLES_FILE.stat().st_size > 0:
            with open(VEHICLES_FILE, "r", encoding="utf-8") as file:
                existing_vehicles = json.load(file)

            updated = False
            for item in existing_vehicles:
                if item.get("plate_number") == vehicle.plate_number:
                    item["condition"] = condition
                    updated = True
                    break

            if updated:
                with open(VEHICLES_FILE, "w", encoding="utf-8") as file:
                    json.dump(existing_vehicles, file, indent=4)

        # 3. Create and queue the report
        report = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "mechanic_id": self.id,
            "mechanic_name": self.name,
            "plate_number": vehicle.plate_number,
            "vin": vehicle.vin,
            "condition": condition,
        }

        Mechanic.reports.append(report)
        return report

    def save_report(self):
        if REPORTS_FILE.exists() and REPORTS_FILE.stat().st_size > 0:
            with open(REPORTS_FILE, "r", encoding="utf-8") as file:
                existing_reports = json.load(file)
        else:
            existing_reports = []

        existing_reports.extend(Mechanic.reports)
        Mechanic.reports.clear()

        with open(REPORTS_FILE, "w", encoding="utf-8") as file:
            json.dump(existing_reports, file, indent=4)
