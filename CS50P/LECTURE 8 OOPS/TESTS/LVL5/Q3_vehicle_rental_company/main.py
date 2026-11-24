import json
from pathlib import Path
from models import Vehicle, Customer, Mechanic, VEHICLES_FILE, REPORTS_FILE
from vehicle_system import ManagementSystem

SALES_FILE = ManagementSystem.sales_file


def reset_test_files():
    """Start with a clean slate before running tests."""
    for file_path in (VEHICLES_FILE, REPORTS_FILE, SALES_FILE):
        if file_path.exists():
            file_path.unlink()
    Vehicle.vehicles.clear()
    Mechanic.reports.clear()


def expect_error(label: str, func, *args, **kwargs):
    """Helper to verify that invalid actions raise the expected exception."""
    try:
        func(*args, **kwargs)
        print(f"[FAIL] {label} -> Expected an error, but none was raised!")
    except (ValueError, TypeError) as err:
        print(f"[PASS] {label} -> Caught {type(err).__name__}: {err}")


def print_json_file(title: str, path: Path):
    print(f"\n--- {title} ({path.name}) ---")
    if path.exists():
        print(path.read_text(encoding="utf-8"))
    else:
        print("File does not exist.")


def run_tests():
    reset_test_files()
    system = ManagementSystem()
    print("=== STARTING RIGOROUS SYSTEM TESTS ===\n")

    # 1. Validation stress tests on Vehicle, Customer, and Mechanic creation
    expect_error(
        "Invalid Nigerian Plate Number",
        Vehicle, "123-INVALID", "Toyota", "Camry", 2020, "black",
        "1HGBH41JXMN109186", "sedan", 1, 5_000_000
    )
    expect_error(
        "Fake Car Make/Model via NHTSA API",
        Vehicle, "LAG-101AA", "NotACarBrand", "FakeModel", 2020, "black",
        "1HGBH41JXMN109186", "sedan", 1, 5_000_000
    )
    expect_error(
        "Fake Color via Color Pizza API",
        Vehicle, "LAG-101AA", "Toyota", "Camry", 2020, "notarealcolorxyz",
        "1HGBH41JXMN109186", "sedan", 1, 5_000_000
    )
    expect_error(
        "Invalid VIN (contains forbidden letter 'I')",
        Vehicle, "LAG-101AA", "Toyota", "Camry", 2020, "black",
        "1HGBH41JXMN10918I", "sedan", 1, 5_000_000
    )
    expect_error(
        "Price below 200,000 Naira",
        Vehicle, "LAG-101AA", "Toyota", "Camry", 2020, "black",
        "1HGBH41JXMN109186", "sedan", 1, 150_000
    )
    expect_error(
        "Invalid Customer Phone (not +234 format)",
        Customer, "Chinedu Okafor", "ABC12345DE67", "12345678901", "08012345678"
    )
    expect_error(
        "Invalid Mechanic Worker ID",
        Mechanic, "Tunde Bakare", "WORKER-01"
    )

    # 2. Create valid objects and register vehicles
    print("\n--- Registering Valid Vehicles & Staff ---")
    car_1 = Vehicle(
        plate_number="KJA-234AB",
        make="Toyota",
        model="Camry",
        year=2021,
        color="black",
        vin="4T1B11HK5JU123456",
        vehicle_type="sedan",
        quantity=1,
        price=8_500_000
    )
    car_2 = Vehicle(
        plate_number="ABJ-999XY",
        make="Honda",
        model="Civic",
        year=2022,
        color="white",
        vin="2HGFC2F59NH543210",
        vehicle_type="sedan",
        quantity=2,  # Quantity of 2 to test decrementing vs deleting
        price=10_000_000
    )
    unregistered_car = Vehicle(
        plate_number="PHC-555ZZ",
        make="Ford",
        model="Explorer",
        year=2019,
        color="blue",
        vin="1FM5K8D84KGA11111",
        vehicle_type="suv",
        quantity=1,
        price=12_000_000
    )

    system.register_vehicle(car_1)
    system.register_vehicle(car_2)
    print("[PASS] Registered car_1 (qty=1) and car_2 (qty=2) to vehicles.json")

    customer_1 = Customer("Amina Yusuf", "LAG12345AB12", "12345678901", "+2348012345678")
    customer_2 = Customer("Emeka Nwosu", "ABJ98765CD34", "98765432109", "+2347098765432")
    mechanic = Mechanic("Seyi Adeyemi", "MECH-001")

    # 3. Mechanic workflow & unassigned check
    expect_error(
        "Mechanic making report before vehicle is assigned",
        mechanic.make_report, car_1, "Damaged"
    )

    mechanic.assign_vehicle(car_1)
    mechanic.make_report(car_1, "Damaged")
    mechanic.save_report()
    print("[PASS] Mechanic marked car_1 as 'Damaged' and synced to vehicles.json & reports.json")

    # 4. Selling edge cases (wrong plate, damaged car, wrong amount)
    expect_error(
        "Selling a vehicle not in vehicles.json",
        system.sell_vehicle, customer_1, unregistered_car, 12_000_000
    )
    expect_error(
        "Selling a 'Damaged' vehicle",
        system.sell_vehicle, customer_1, car_1, 8_500_000
    )
    expect_error(
        "Selling with wrong payment amount",
        system.sell_vehicle, customer_1, car_2, 5_000_000
    )

    # 5. Repair car_1 and complete sale (should remove car_1 from vehicles.json since qty=1)
    mechanic.make_report(car_1, "Good")
    mechanic.save_report()
    system.sell_vehicle(customer_1, car_1, 8_500_000)
    print("[PASS] Repaired car_1 -> Sold to customer_1 -> Removed from vehicles.json")

    # 6. Sell 1 unit of car_2 (qty=2 -> should decrement to qty=1, NOT delete)
    system.sell_vehicle(customer_2, car_2, 10_000_000)
    print("[PASS] Sold 1 unit of car_2 -> Quantity decremented to 1 in vehicles.json")

    # 7. Simulate program restart (new ManagementSystem instance) & sell last unit of car_2
    new_system = ManagementSystem()
    new_system.sell_vehicle(customer_1, car_2, 10_000_000)
    print("[PASS] After simulated restart, sold final unit of car_2 -> vehicles.json now empty")

    # 8. Inspect final JSON outputs
    print_json_file("FINAL INVENTORY", VEHICLES_FILE)
    print_json_file("FINAL REPORTS", REPORTS_FILE)
    print_json_file("FINAL SALES", SALES_FILE)


if __name__ == "__main__":
    run_tests()
