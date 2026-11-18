"""
Functions :
    Function in python is reusable block of code that performs specific task and runs only when called.
    Function defined using the def keyword.
    Functions help organize programs into smaller pieces, improve readability, and prevent code repetition.

Syntax :
    def Function_name(Args):
        //LOC 
"""

def greet():
    print("Hello!")
    print("Welcome to Python")

# greet()


def greet(name):
    print(f"Hello, {name}!")

# greet("Naman")


def add(a, b):
    return a + b

# print(add(4, 5))


def is_even(n):
    return n % 2 == 0

# print(is_even(4))
# print(is_even(7))


def grade(marks):
    if marks >= 40:
        return "Pass"
    return "Fail"

# print(grade(55))
# print(grade(30))


def intro(name, age, city="Pune"):
    return f"{name}, {age}, {city}"

# print(intro("Rahul", 25, city="Mumbai"))
# print(intro(age=20, name="Aisha"))