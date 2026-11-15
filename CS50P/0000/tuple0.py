latitude, longitude = map(float, input("Enter latitude and longitude separated by a space: ").split())
coordinates = (latitude, longitude)
print(f"{coordinates}")

coordinates = latitude, longitude
print(f"Latitude: {latitude},\nLongitude: {longitude}")
print(coordinates[0],coordinates[1])

name, country = input("Your name, country: ").split()
age = int(input("Age: "))
person = (name, age, country)
person  = name, age, country
print(person)
c, i = country.split()
p = c, i
print(c)