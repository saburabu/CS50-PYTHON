from pathlib import Path
import sys

father_folder = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(father_folder))


import pytest
from unittest.mock import patch
from models import Vehicle, Customer, Mechanics  



# ==========================================
# FIXTURES (Mock APIs so tests run fast & offline)
# ==========================================
@pytest.fixture
def mock_apis():
    def fake_make_model(make: str, model: str) -> bool:
        valid = {
            "toyota": {"camry", "corolla", "rav4"},
            "honda": {"civic", "accord"},
        }
        return model.strip().lower() in valid.get(make.strip().lower(), set())

    def fake_color(color: str) -> bool:
        return color.strip().lower() in {"black", "white", "red", "blue", "silver"}

    with patch.object(Vehicle, "is_valid_make_model", side_effect=fake_make_model), \
         patch.object(Vehicle, "is_valid_color_api", side_effect=fake_color):
        yield


@pytest.fixture
def sample_vehicle(mock_apis):
    return Vehicle(
        plate_number="LAG-123AB",
        make="Toyota",
        model="Camry",
        year=2020,
        color="black",
        vin="1HGCM82633A004352",
        vehicle_type="sedan",
        quantity=2,
        price=5000000,
    )


# ==========================================
# 1–5: VALID "HAPPY PATH" & BOUNDARY TESTS
# ==========================================
def test_01_valid_vehicle_normalization(mock_apis):
    car = Vehicle("lag-123ab", "toyota", "camry", 2020, "black", "1HGCM82633A004352", "sedan", 2, 5000000)
    assert car.plate_number == "LAG-123AB"
    assert car.make == "Toyota"
    assert car.model == "Camry"
    assert car.condition == "Good"


def test_02_plate_without_hyphen_and_whitespace(mock_apis):
    car = Vehicle("  ABC456XY  ", "Honda", "Civic", 2022, "White", "2T1BURHE0JC034123", "SEDAN", 1, 200000, "12345678901")
    assert car.plate_number == "ABC456XY"
    assert car.price == 200000
    assert car.owner_nin == "12345678901"


def test_03_year_boundaries(mock_apis):
    old_car = Vehicle("LAG-111AA", "Toyota", "Corolla", 1900, "red", "1HGCM82633A004352", "sedan", 1, 250000)
    new_car = Vehicle("LAG-222BB", "Toyota", "Camry", 2027, "blue", "2T1BURHE0JC034123", "sedan", 1, 250000)
    assert old_car.year == 1900
    assert new_car.year == 2027


def test_04_three_part_customer_name(sample_vehicle):
    cust = Customer("chinedu okafor mensah", "lag12345ab12", "12345678901")
    cust.add_car(sample_vehicle)
    assert cust.name == "Chinedu Okafor Mensah"
    assert cust.dln == "LAG12345AB12"
    assert len(cust.vehicles) == 1


def test_05_mechanic_workflow(sample_vehicle):
    mech = Mechanics("emeka obi", "mech-001")
    mech.assign_vehicle(sample_vehicle)
    report = mech.make_report(sample_vehicle, "Needs Maintenance", "  Brake pads worn  ")
    assert sample_vehicle.condition == "Needs Maintenance"
    assert report["notes"] == "Brake pads worn"
    assert report["mechanic_id"] == "MECH-001"


# ==========================================
# 6–15: VEHICLE EDGE CASES (Should Raise ValueError)
# ==========================================
@pytest.mark.parametrize("bad_plate", ["LA-1234AB", "LAG-1234B", "123-ABC45", "", 12345])
def test_06_invalid_plate_numbers(mock_apis, bad_plate):
    with pytest.raises(ValueError):
        Vehicle(bad_plate, "Toyota", "Camry", 2020, "black", "1HGCM82633A004352", "sedan", 1, 500000)


@pytest.mark.parametrize("bad_vin_char", ["1HGCM82633I004352", "1HGCM82633O004352", "1HGCM82633Q004352"])
def test_07_vin_forbidden_characters(mock_apis, bad_vin_char):
    with pytest.raises(ValueError):
        Vehicle("LAG-123AB", "Toyota", "Camry", 2020, "black", bad_vin_char, "sedan", 1, 500000)


@pytest.mark.parametrize("bad_vin_len", ["1HGCM82633A00435", "1HGCM82633A0043529"])
def test_08_vin_wrong_length(mock_apis, bad_vin_len):
    with pytest.raises(ValueError):
        Vehicle("LAG-123AB", "Toyota", "Camry", 2020, "black", bad_vin_len, "sedan", 1, 500000)


def test_09_booleans_rejected_for_numbers(mock_apis):
    with pytest.raises(ValueError):
        Vehicle("LAG-123AB", "Toyota", "Camry", True, "black", "1HGCM82633A004352", "sedan", 1, 500000)
    with pytest.raises(ValueError):
        Vehicle("LAG-123AB", "Toyota", "Camry", 2020, "black", "1HGCM82633A004352", "sedan", True, 500000)
    with pytest.raises(ValueError):
        Vehicle("LAG-123AB", "Toyota", "Camry", 2020, "black", "1HGCM82633A004352", "sedan", 1, True)


@pytest.mark.parametrize("bad_year", [1899, 2028, "2020", 2020.5])
def test_10_invalid_years(mock_apis, bad_year):
    with pytest.raises(ValueError):
        Vehicle("LAG-123AB", "Toyota", "Camry", bad_year, "black", "1HGCM82633A004352", "sedan", 1, 500000)


def test_11_price_below_minimum(mock_apis):
    with pytest.raises(ValueError):
        Vehicle("LAG-123AB", "Toyota", "Camry", 2020, "black", "1HGCM82633A004352", "sedan", 1, 199999.99)


@pytest.mark.parametrize("bad_qty", [0, -1, -10])
def test_12_invalid_quantity(mock_apis, bad_qty):
    with pytest.raises(ValueError):
        Vehicle("LAG-123AB", "Toyota", "Camry", 2020, "black", "1HGCM82633A004352", "sedan", bad_qty, 500000)


def test_13_mismatched_make_and_model(mock_apis):
    # Toyota does not make Civic
    with pytest.raises(ValueError):
        Vehicle("LAG-123AB", "Toyota", "Civic", 2020, "black", "1HGCM82633A004352", "sedan", 1, 500000)


def test_14_invalid_color(mock_apis):
    with pytest.raises(ValueError):
        Vehicle("LAG-123AB", "Toyota", "Camry", 2020, "blak", "1HGCM82633A004352", "sedan", 1, 500000)


@pytest.mark.parametrize("bad_nin", ["1234567890", "123456789012", "1234567890a", 12345678901])
def test_15_invalid_owner_nin(mock_apis, bad_nin):
    with pytest.raises(ValueError):
        Vehicle("LAG-123AB", "Toyota", "Camry", 2020, "black", "1HGCM82633A004352", "sedan", 1, 500000, bad_nin)


# ==========================================
# 16–20: CUSTOMER & MECHANICS EDGE CASES
# ==========================================
@pytest.mark.parametrize("bad_name", ["Tunde", "Adebayo Oluwaseun Chidi Musa"])
def test_16_customer_name_word_count(bad_name):
    with pytest.raises(ValueError):
        Customer(bad_name, "LAG12345AB12", "12345678901")


@pytest.mark.parametrize("bad_name", ["John  Doe", "John Doe2", "John-Doe Smith"])
def test_17_customer_name_characters_and_spacing(bad_name):
    with pytest.raises(ValueError):
        Customer(bad_name, "LAG12345AB12", "12345678901")


@pytest.mark.parametrize("bad_dln", ["LA12345AB12", "LAG1234AB12", "LAG12345A12", "LAG12345AB1"])
def test_18_invalid_driver_license(bad_dln):
    with pytest.raises(ValueError):
        Customer("John Doe", bad_dln, "12345678901")


def test_19_mechanic_reporting_unassigned_vehicle(mock_apis, sample_vehicle):
    car2 = Vehicle("ABJ-999ZZ", "Honda", "Accord", 2021, "white", "2T1BURHE0JC034123", "sedan", 1, 600000)
    mech = Mechanics("Seyi Adeyemi", "MECH-007")
    mech.assign_vehicle(sample_vehicle)

    with pytest.raises(ValueError):
        mech.make_report(car2, "Damaged", "Broken windshield")


def test_20_wrong_object_type_passed():
    cust = Customer("John Doe", "LAG12345AB12", "12345678901")
    mech = Mechanics("Seyi Adeyemi", "MECH-007")

    with pytest.raises(ValueError):
        cust.add_car({"make": "Toyota"})
    with pytest.raises(ValueError):
        mech.assign_vehicle("LAG-123AB")
    with pytest.raises(ValueError):
        mech.make_report("LAG-123AB", "Good", "All fine")

def test_live_apis():
    assert Vehicle.is_valid_make_model("Toyota", "Camry") is True
    assert Vehicle.is_valid_make_model("Toyota", "FakeModel123") is False
    assert Vehicle.is_valid_color_api("red") is True
    assert Vehicle.is_valid_color_api("notacolorxyz") is False
