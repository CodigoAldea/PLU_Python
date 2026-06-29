#  Create a Student class with name and age, then display them.

class Student:
    def __init__(self, n, a):
        self.name = n
        self.age = a

obj = Student("Ram", 20)

print(obj.name)
print(obj.age)