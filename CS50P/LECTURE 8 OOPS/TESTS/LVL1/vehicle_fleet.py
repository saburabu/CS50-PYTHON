class Vehicle:
    def __init__(self, registration_number, brand, initial_fuel, odometer_mileage, max_tank_capacity=50):
        self.reg = registration_number
        self.brand = brand                      # sorry i change fuel_level to initial_fuel
        self.fuel = initial_fuel              # Current fuel in liters
        self.max_capacity = max_tank_capacity  # Maximum tank limit (default 50L)
        self.mileage = odometer_mileage        # Total distance driven in km
        self.fuel_efficiency = 10              # Fixed: 10 km per 1 liter (10km/L)

    def refuel(self, liters_to_add):
        if liters_to_add <= 0:
            return "Error: Quantity must be greater than 0!"
            
        # Calculate how much space is left in the tank based on internal capacity
        space_left = self.max_capacity - self.fuel
        
        if liters_to_add > space_left:
            return f"Error: {liters_to_add}L exceeds available tank space of {space_left}L (Max: {self.max_capacity}L)."
            
        # Add liters strictly to the fuel attribute
        self.fuel += liters_to_add
        return f"Refueled successfully! Current fuel level: {self.fuel}L"

    def travel(self, distance_km):
        if distance_km <= 0:
            return "Error: Distance must be greater than 0km."
            
        # 1. Calculate how many liters are needed using internal math rule (distance / 10)
        fuel_needed = distance_km / self.fuel_efficiency

        # 2. Check if the car has enough fuel
        if self.fuel == 0 or self.fuel <= 2:  # Safe low fuel warning zone
            return "⚠️ KINDLY REFUEL YOUR CAR! Fuel level critically low."
            
        if fuel_needed > self.fuel:
            return f"❌ Insufficient fuel! You need {fuel_needed}L to travel {distance_km}km, but you only have {self.fuel}L."

        # 3. Perform physics update if checks pass
        self.fuel -= fuel_needed       # Fuel level decreases
        self.mileage += distance_km    # Lifetime mileage tracker increases
        
        return (f"🚗 [{self.brand} - {self.reg}]\n"
                f"• Travelled: {distance_km}km\n"
                f"• Used: {fuel_needed}L of fuel\n"
                f"• Remaining Fuel: {self.fuel}L\n"
                f"• Lifetime Odometer: {self.mileage}km")

# --- Interactive Test Suite ---
# Initial Setup: Car has 15L of fuel, starting mileage is 12,000km, max tank holds 50L
my_car = Vehicle("LAG-889-AA", "Toyota Corolla", 15, 12000, max_tank_capacity=50)
my_car1 = Vehicle("LAG-889-AA", "Toyota Camry", 15, 12000, max_tank_capacity=50)
my_car2 = Vehicle("LAG-889-AA", "Toyota RAV4", 15, 12000, max_tank_capacity=50)
my_car3 = Vehicle("LAG-889-AA", "Toyota Highlander", 15, 12000, max_tank_capacity=50)

# Test 1: Successful travel
print(my_car.travel(100))  # Should use exactly 10 Liters (leaving 5L)

# Test 2: Attempting an impossible long trip with low fuel
print("\n" + my_car.travel(300)) 

# Test 3: Overfilling the gas tank
print("\n" + my_car.refuel(60))

# Test 4: Correct Refuel operation
print("\n" + my_car.refuel(20)) # Adds 20L to the remaining 5L = 25L

# Test 5: Standard travel post-refuel
print("\n" + my_car.travel(150)) # Should use 15L, leaving 10L on a total mileage of 12,250km
