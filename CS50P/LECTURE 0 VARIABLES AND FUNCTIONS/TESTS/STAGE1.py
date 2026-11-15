# CHALLLENGE 1

first = input("what is your firstname?: ")
last = input("what is your lastname?: ")

def get_full_name(first, last):
    full_name = first.strip().title() + " " + last.strip().title()
    return full_name

def introduce(name):
    print(f"hi there,{name},nice to meet you")

name = full_name = get_full_name(first, last)

introduce(name)
