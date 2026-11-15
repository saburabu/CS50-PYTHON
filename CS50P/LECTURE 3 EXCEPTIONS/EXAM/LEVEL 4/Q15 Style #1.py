contacts = {}

def add_contact():
    while True:
        name = str(input("Name: "))
        while True:
            try:
                phone_number = int(input("Number: "))
            except ValueError as a:
                print(f"ENTER A NUMBER{a}")
            else:
                break

        if name in contacts:
            print("CONTACT ALREADY EXISTS")
        else:
            contacts[name] = phone_number
            break

def find_contact():
    name = str(input("Name: "))
    phone = contacts.get(name)
    if phone is None:
        print("Contact not found")
    else:
        print(phone)

def delete_contact():
    name = str(input("Name: "))
    if name in contacts:
        del contacts[name]
        print(f"{name}'s contact has been deleted")
    else:
        print("Not in contacts")

def show_contact():
    for name , phone in contacts.items():
        print(name, phone)

while True:
    print("1.Add contacts\n2.Find contacts\n3.Delete contacts\n4.Show all contacts\n5.Quit")
    choice = str(input("CHOICE: "))

    if choice == "1":
        add_contact()
    elif choice == "2":
        find_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        show_contact()
    elif choice == "5":
        break
    else:
        print("INVALID TRY AGAIN")
        pass
        