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

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Rahul", 21)
student2 = Student("Priya", 22)

# print(student1.name)
# print(student1.age)

# print(student2.name)
# print(student2.age)


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print(self.name, "is studying")


student1 = Student("Rahul", 21)

# student1.study()


# Shopping cart management :
class ShoppingCart:
    
    def details(self, name, product, price, quantity):
        self.name = name
        self.product = product
        self.price = price
        self.quantity = quantity

   
    def calculate_total(self):
        self.total = self.price * self.quantity

   
    def apply_discount(self):
        if self.total > 5000:
            self.final_bill = self.total * 0.90  
        else:
            self.final_bill = self.total         

   
    def display_bill(self):
        print(f"Name: {self.name}")
        print(f"Product: {self.product}")
        print(f"Final Bill: {self.final_bill}")



# cart = ShoppingCart()
# cart.details("Rahul", "Laptop", 6000, 1)
# cart.calculate_total()
# cart.apply_discount()
# cart.display_bill()



# Liabrary Book Management
class LiabraryBook():

    def set_details(self, book, author, price):
        self.book = book
        self.author = author
        self.price = price
        self.available = True

    def issue_book(self):
        if self.available:
            self.available = False
            print(f"'{self.book}' has been issued.")
        else:
            print(f"Sorry, '{self.book}' is currently not available.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"'{self.book}' has been returned.")
        else:
            print(f"'{self.book}' is already available.")
            
    def display_info(self):
        status = "Available" if self.available else "Not Available"
        print(f"Book: {self.book}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
        print(f"Availability: {status}")

# b1 = LiabraryBook()
# b1.set_details("Python Basics", "John Doe", "1200")
# b1.display_info()
# b1.issue_book()
# b1.display_info


# ------------------------------------------------------------------------------------------------------------------------------------------------


        

