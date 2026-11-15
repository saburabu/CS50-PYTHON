user_name = str(input("Username: "))
pin = int(input("Pin: ")) 
country = str(input("Country: "))

user_name = user_name.strip().title()
country = country.strip().title()

if ("Sabur" in user_name) and (pin in [2468]) and ("Nigeria" or "Ghana" in country):
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")