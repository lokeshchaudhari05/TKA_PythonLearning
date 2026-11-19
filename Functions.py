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


#-------------------------------------------------------------------------------------------------------------------------------------------------
# Positional Arguments (*args) & Keyword Arguments (**kwargs)
"""
Positional Argument :
    A positional argument is a value passed to a function whose meaning is determined strictly by its order (position) in the function call.
    The first value you pass is assigned to the first parameter in the function definition, the second value goes to the second parameter, and so on.
    Defined as *args.

Syntax :
    def show(*items):
    for item in items:
        print(item)

show("pen", "book", "bag")
"""

"""
Keyword Arguments :
    A keyword argument (often shortened to kwarg) is a value passed to a Python function by explicitly naming the parameter it belongs to, using the key=value syntax. 
    returns result in dictionary.
    defined by **kwargs.

Syntax :
    def greet(name, message):
        print(f"{message}, {name}!")     

    greet(name="Alice", message="Welcome")
"""

"""
LOCAL & GLOBAL VARIABLE :
    Local Variable :
        A variable created inside a function is local. It exists only while the function runs.
        Example :
            def test():
                 x = 10
            print("inside:", x)

        test()


    Global Variable :
        A variable created outside every function is global. Functions can read it.
        Example :
            rate = 10

            def show():
                print("rate is", rate)

            show()

"""

"""
Nested Function :
    A nested function (also called an inner function) is a function defined inside the body of another function. It exists only within the local scope of its enclosing (outer) function and cannot be called directly from outside it.

    Example :
        def outer_function(name):
    
            def inner_function():
                print(f"Hello, {name}!")
    
    
            inner_function()
        outer_function("Alice")

"""