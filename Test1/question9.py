# Create a Student class with name and age, then display them.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Tanvi", 21)

print("Name:", s.name)
print("Age:", s.age)

