shopping_list = ["Rice", "Beans", "Milk"]
my_list = shopping_list

my_list.append("Bread")
print(shopping_list)

shopping_list.remove("Milk")
print(my_list)

print(my_list is shopping_list)
"""
    because basically {my_list} is making reference to the same object as {shopping_list} so any change
    to any of them causes the other to change
"""