"""
Encapsulation :
    Encapsulation is object-oriented programming concept.
    Encapsulation refers to the binding of data and methods in the class.
    It also helps control how data is accessed and modified.

"""

class Student:

    def __init__(self, name, age):
        self.name = name
        self.__age = age  

    def display_details(self):
        print("Student Name:", self.name)
        print("Student Age:", self.__age)

    def get_age(self):
        return self.__age



student1 = Student("Lokesh", 20)
print("Name:", student1.name)
print("Age:", student1.get_age())
student1.display_details()