# TEMPERATURE CONVERTER
tempt = input_temperature = float(input("Enter temperature in Celsius: "))
# where the conversion is calculated and returned
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
#where the conversion is calculated and printed
fahrenheit = celsius_to_fahrenheit(tempt)
print(f"{tempt}°C is equal to {fahrenheit:.2f}°F")
print("Thank you for using the Temperature Converter!")