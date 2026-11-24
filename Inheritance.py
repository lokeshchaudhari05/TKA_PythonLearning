"""
Inheritance :
    Inheritance is OOP feature.
    In this the new clss(Child/sub) is based on the existing class(Parent/super).
    The child class can reuse accessible attributes and methods from the parent and can add or customize it's behaviour.
    Simply, child class inherits the features of the parent class.
    It is also known as IS-A Relationship.
    

Syntax :
    class Parent():
        # attributes and methods
        pass
        
    class Child(Parent):
        # additional attributes & methods
        pass

"""

# class Animal():
#     def eating(self):
#         print("Animal is eating ")

#     def sleeping(self):
#         print("Animal sleeping")

# class Dog(Animal):
#     def sound(self):
#         print("Dog is Barking ")            

# class Cat(Animal):
#     def sound(self):
#         print("cat --> meow ")

# d = Dog()
# d.eating()
# d.sleeping()
# d.sound()

# c = Cat()
# c.eating()
# c.sleeping()
# c.sound()

# ----------------------------------------------------------------------------------------------------------------------------------

# class Father():
#       def cooking(self):
#             print("Father --> Non veg ")

# class Mother():
#       def cooking(self):
#             print("Mother --> Veg ")



# class Son(Mother,Father):
#      pass
             
# s = Son()
# s.cooking()  ----> Son is getting the mother's cooking feature beacuse of first decleration is mother,father in parameter.
#                    (Method Resolution Method)      

# -------------------------------------------------------------------------------------------------------------------------------------


#  Related Constructor


# class Demo():

#      def __init__(self,name,city):
#           self.name = name
#           self.city = city
#           print("Cosntr of Parent --> ",name,city )


# class Day(Demo):

#      def __init__(self,name,city): 
#         super().__init__(name,city)
#         print("Name --> ",name,"City --> ",city)
         
    
# d = Day("Praful","goa")

# ---------------------------------------------------------------------------------------------------------------------------------------

# Create Hospital class with hospital_name and location. create a doctor child class with doctor_name and specialization :

# class Hospital:
#     def __init__(self, H_name, H_city):
#         self.name = H_name
#         self.city = H_city

# class Doctor(Hospital):
#     def __init__(self, H_name, H_city, d_name, d_specialization):
#         super().__init__(H_name, H_city)
#         self.dname = d_name
#         self.specialization = d_specialization

#     def display(self):
#         print("Hospital Name:", self.name)
#         print("City:", self.city)
#         print("Doctor Name:", self.dname)
#         print("Specialization:", self.specialization)

# d1 = Doctor("Orchid", "Jalgaon", "xyz", "abc")
# d1.display()

# ------------------------------------------------------------------------------------------------------------------------------------------

# Create a class Product with product_id and prodcut_name.create electronic_products with warranty_years.

# class Product():
    
#     def __init__(self, product_id, product_name):
#         self.id = product_id
#         self.name = product_name

# class Electronic_product(Product):

#     def __init__(self, product_id, product_name, warranty_year):
#         super().__init__(product_id, product_name)
#         self.warranty = warranty_year

#     def display(self):
#         print("Product Id: ",self.id)
#         print("Product Name: ",self.name)
#         print("Warranty Year: ",self.warranty)

# p = Electronic_product(123, "Laptop", "2-years")
# p.display()

# ----------------------------------------------------------------------------------------------------------------------------------------

# create two parent classes music player and camera. create a smartdevice child that inherits both.

# class MusicPlayer:
#     def play_music(self):
#         print("Playing music")

# class Camera:
#     def take_photo(self):
#         print("Taking photo")

# class SmartDevice(MusicPlayer, Camera):
#     pass

# # Usage
# device = SmartDevice()
# device.play_music()
# device.take_photo()

# -------------------------------------------------------------------------------------------------------------------------------------------

# Create Animal --> mammal --> Dog using multilevel inheritance.

# class Animal:
#     def eat(self):
#         print("Eating")

# class Mammal(Animal):
#     def walk(self):
#         print("Walking")

# class Dog(Mammal):
#     def bark(self):
#         print("Barking")


# dog = Dog()
# dog.eat()  
# dog.walk()  
# dog.bark() 

# ----------------------------------------------------------------------------------------------------------------------------------------------

# Create a school as parent and teacher, student and office_staff as child class 

# class School:
#     def attend(self):
#         print("Attending school")

# class Teacher(School):
#     def teach(self):
#         print("Teaching class")

# class Student(School):
#     def study(self):
#         print("Studying lessons")

# class OfficeStaff(School):
#     def manage(self):
#         print("Managing records")


# teacher = Teacher()
# teacher.attend()
# teacher.teach()

# student = Student()
# student.attend()
# student.study()

# staff = OfficeStaff()
# staff.attend()
# staff.manage()

# ----------------------------------------------------------------------------------------------------------------------------------------

# Create Athlet, person and student. create studentathlet inheriting athlet and student.

# class Person:
#     def breathe(self):
#         print("Breathing")

# class Athlete(Person):
#     def train(self):
#         print("Training")

# class Student(Person):
#     def study(self):
#         print("Studying")

# class StudentAthlete(Athlete, Student):
#     def balance(self):
#         print("Balancing sports and studies")


# sa = StudentAthlete()
# sa.breathe()  
# sa.train()    
# sa.study()  
# sa.balance()  

# -------------------------------------------------------------------------------------------------------------------------------------------

# create a parent class with parameterized initilizer and pass values from the child using super. 

# class Person:
#     def __init__(self, name):
#         self.name = name

# class Student(Person):
#     def __init__(self, name, grade):
#         super().__init__(name)  
#         self.grade = grade


# s = Student("Aarav", "A")
# print(s.name)  
# print(s.grade)

# -------------------------------------------------------------------------------------------------------------------------------------------
 
# create a parent method calculate_salary().override it in permanantEmployee and contractEmployee.

# class Employee:
#     def calculate_salary(self):
#         print("Base salary")

# class PermanentEmployee(Employee):
#     def calculate_salary(self):
#         print("Monthly fixed salary")

# class ContractEmployee(Employee):
#     def calculate_salary(self):
#         print("Hourly contract salary")


# p = PermanentEmployee()
# c = ContractEmployee()

# p.calculate_salary()  
# c.calculate_salary() 

# --------------------------------------------------------------------------------------------------------------------------------------------

# Create two parent classes with a method named info().inspect the child class MRO and explain which method is executed.

# class ParentA:
#     def info(self):
#         print("Info from ParentA")

# class ParentB:
#     def info(self):
#         print("Info from ParentB")

# class Child(ParentB, ParentA):
#     pass


# c = Child()
# c.info()           

# ----------------------------------------------------------------------------------------------------------------------------------------------