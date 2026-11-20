"""
OOP :
    OOP stands for the object oriented programming. 
    It is an programming approach where we organise the code using Classes & Objects.
    OOP allows us to combine data (variables) and behaviour (functions) into one structure.
    OOP provides Organisation, Reusability, Scalability, Real-world modelling.
    In oop functions defined inside the class called as methods.

Real-World understanding : Class & Objects
    1] Class :
        A class in OOP is user defined blueprint or template used to create a object. 
        A class can contain the attributes(data/variables) and methods(function defined inside the class).

        Syntax :
            class class_name():
                //Attributes
                //methods
            pass


    2] Object :
        An object is an instance of class.
        We create the object by calling the class name with the paranthesis.
        The paranthesis here simply creates the instance instance using python's default object-creation behaviour.

        Example :
            class Student():
                def display(self):
                    print("I am student")

            student1 = Student()
            student2 = student()

            student1.display()
            student2.display()

            
SELF :
    Self refers to the current object that is calling the method.
    It alllows the method to access that perticular object's attributes and other methods.
                  
"""

# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# student1 = Student("Rahul", 21)
# student2 = Student("Priya", 22)

#  print(student1.name)
#  print(student1.age)

#  print(student2.name)
#  print(student2.age)



# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def study(self):
#         print(self.name, "is studying")


# student1 = Student("Rahul", 21)
# student1.study()

# create a class calculator, store two numbers and createv different methods for the addition, subtraction, multiplication & dividation
# class Calculator():
#     def op(self, number1, number2):
#         self.num1 = number1
#         self.num2 = number2

#     def Addition(self):
#         print(f'Addition of two number is: {self.num1 + self.num2}')
#     def Subtraction(self):
#         print(f'Subtraction of two number is: {self.num1 - self.num2}')
#     def multiplication(self):
#         print(f'Multiplication of two number is: {self.num1 * self.num2}')
#     def Dividation(self):
#         print(f'Dividation of two number is: {self.num1 / self.num2}')

# c1 = Calculator()
# c1.op(16, 8)
# c1.Addition()
# c1.Subtraction()
# c1.multiplication()
# c1.Dividation()



# store one number. check whether it is positive,negative or zero.
# class Num_check():
#     def info(self, number):
#         self.num1 = number

#     def check(self):
#         if self.num1 == 0:
#             print(f'{self.num1} is zero')
#         elif self.num1 < 0 :
#             print(f'{self.num1} is Negative number')
#         else :
#             print(f'{self.num1} is Positive number')

# c1 = Num_check()
# c1.info(int(input("Enter the number: ")))
# c1.check()



# class ATM():
#     def __init__(self, balance = 0):
#         self.balance = balance

#     def Check_balance(self):
#         return self.balance

#     def deposit(self, amount):
#         if amount <= 0 :
#             print("Invalid Amount")
#         else: 
#             self.balance += amount
#             print(f'Deposited: {amount}')
#             print(f'Available Balance: {self.balance}')

#     def Withdraw(self, amount):
#         if amount <= 0:
#             print("Invalid Amount")
#         elif amount > self.balance :
#             print("Insufficient Balance")
#         else:
#             self.balance -= amount
#             print(f'{amount} Withdraw Successfully')
#             print(f'Available Balance: {self.balance}')

#     def Updated_balance(self):
#         print(f'Updated balance is {self.balance}')

# w1 = ATM()
# w1.Check_balance()
# w1.deposit (7000)
# w1.Withdraw(2000)
# w1.Updated_balance()



# Shopping cart management :
# class ShoppingCart:
    
#     def details(self, name, product, price, quantity):
#         self.name = name
#         self.product = product
#         self.price = price
#         self.quantity = quantity

   
#     def calculate_total(self):
#         self.total = self.price * self.quantity

   
#     def apply_discount(self):
#         if self.total > 5000:
#             self.final_bill = self.total * 0.90  
#         else:
#             self.final_bill = self.total         

   
#     def display_bill(self):
#         print(f"Name: {self.name}")
#         print(f"Product: {self.product}")
#         print(f"Final Bill: {self.final_bill}")



# cart = ShoppingCart()
# cart.details("Rahul", "Laptop", 6000, 1)
# cart.calculate_total()
# cart.apply_discount()
# cart.display_bill()



# Liabrary Book Management
# class LiabraryBook():

#     def set_details(self, book, author, price):
#         self.book = book
#         self.author = author
#         self.price = price
#         self.available = True

#     def issue_book(self):
#         if self.available:
#             self.available = False
#             print(f"'{self.book}' has been issued.")
#         else:
#             print(f"Sorry, '{self.book}' is currently not available.")

#     def return_book(self):
#         if not self.available:
#             self.available = True
#             print(f"'{self.book}' has been returned.")
#         else:
#             print(f"'{self.book}' is already available.")
            
#     def display_info(self):
#         status = "Available" if self.available else "Not Available"
#         print(f"Book: {self.book}")
#         print(f"Author: {self.author}")
#         print(f"Price: {self.price}")
#         print(f"Availability: {status}")

# b1 = LiabraryBook()
# b1.set_details("Python Basics", "John Doe", "1200")
# b1.display_info()
# b1.issue_book()
# b1.display_info


# ------------------------------------------------------------------------------------------------------------------------------------------------
"""
CONSTRUCTOR (__init__) :
    It is special method in python used to initialize object's data when the object is created.
    It automatically get invoked when object of the class is created.
    It is also called as dunder method.
    Its main purpose is to initialize the object's attributes.
    Constructor directly get called when we create instance of the class but for method we have to call method explicitly.
   
    There are two types of Constructor :
        1] Default Constructor :
            Accepts only self and sets fixed default values.
            self and sets fixed default values. 
            If we don't write an __init__() method at all, Python provides a basic empty one automatically.

            Syntax :
               class ClassName:
                    def __init__(self):  

        2] Constructor with Default Arguments :
            Uses default parameter values, so arguments become optional during object creation.

            Syntax :
                class ClassName:
                    def __init__(self, param1, param2):

"""

# Create a class Student with a default constructor. Print student name, age, and course.
# class student():

#     def __init__(self): #-----> default constructor / automatically get called at the time of object creation
#         self.name = "Ramesh"
#         self.Age = 21
#         self.course = "Python"

#     def display(self):
#         print("Name: ",self.name)
#         print("Age: ",self.Age)
#         print("Course: ",self.course)

# s1 = student()
# s1.display()



# Create a class Employee using a default constructor. Display employee ID, name, and salary.
# class Employee():

#     def __init__(self):
#         self.emp_id = 123
#         self.name = "Sushant"
#         self.salary = 45000

#     def info(self):
#         print("Employee ID: ",self.emp_id)
#         print("Name: ",self.name)
#         print("Salary: ",self.salary)

# e1 = Employee()
# e1.info()



# Create a class Student with a parameterized constructor. Pass student name and marks. Display both details.
# class Student():

#     def __init__(self,student_name,marks):
#         self.student_name = student_name
#         self.marks = marks

#     def display(self):
#         print("Student Name: ", self.student_name)
#         print("Marks: ", self.marks)

# s1 = Student("Vedant", 67)
# s1.display()



# Create a class Rectangle with a parameterized constructor. Pass length and width. Calculate and display the area.
# class Area_rectangle():

#     def __init__(self,length,width):
#         self.length = length
#         self.width = width

#     def area(self):
#         print(f'Area of Reactangle is: {self.length * self.width}')

# a1 = Area_rectangle(8, 5)
# a1.area()



#  Create a class Product with a parameterized constructor. Pass product name, price, and quantity. Calculate and display the total price.
# class Product():
#     def __init__(self,product_name,price,quantity):
#         self.name = product_name
#         self.price = price
#         self.quantity = quantity

#     def total_prize(self):
#         print(f'Product: {self.name}')  
#         print(f'Total price: {self.price * self.quantity}')  

# p1 = Product("Laptop", 75000, 3)
# p1.total_prize()



# Create a class Addition with a parameterized constructor. Pass two numbers and calculate their addition.
# class Addition():

#     def __init__(self,num1,num2):
#         self.number1 = num1
#         self.number2 = num2

#     def addition(self):
#         print(f'Addition of two number is: {self.number1 + self.number2}')

# a1 = Addition(12, 18)
# a1.addition()



# Create a class Number with a parameterized constructor. Pass one number and check whether it is even or odd.
# class Even_odd():
    
#     def __init__(self, number):
#         self.number = number

#     def Iseven(self):
#         if self.number % 2 == 0:
#             print(f'{self.number} is even number')
#         else:
#             print(f'{self.number} is odd number')

# e1 = Even_odd(int(input("Enter the number: ")))
# e1.Iseven()

