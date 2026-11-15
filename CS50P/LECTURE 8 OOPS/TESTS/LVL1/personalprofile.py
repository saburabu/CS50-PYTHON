class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def introduce(self):
        return f"Hello my name is {self.name} am from {self.country}"

person1 = Person("Harry", 16, "Nigeria")
person2 = Person("Sabur", 16, "Nigeria")
person3 = Person("Akuku", 19, "Ghana")

print(f"{person1.introduce()}")
print(f"{person2.introduce()}")
print(f"{person3.introduce()}")