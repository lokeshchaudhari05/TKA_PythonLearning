"""
If Else Statement in python : 

1. What are conditional statements : 

Definition: Conditional statements are decision-making statements that allow a program to execute different blocks of code depending on whether a condition is True or False.
Real-life example: If it rains, take an umbrella. Otherwise, go without one.


types of if else : 

1. simple if statement   --> The if statement executes a block of code only when its condition is True.
2. if else statement  --> if block executes when the condition is true; otherwise, the else block executes.
2. if-elif-else statement --> Python checks them from top to bottom and executes the first block whose condition is true.
4. nested if statement  --> A nested if is an if statement written inside another if or else block. It is useful when one decision depends on another decision.
5. nested if else statement --> A nested if-else is a conditional statement in which an if-else statement is written inside another if or else block. It is used when a second decision depends on the result of the first condition.
6. nested if elif else statement  --> A nested if-elif-else is a conditional structure in which an if-elif-else statement is placed inside another conditional block. It is used when a program must make multiple decisions based on an earlier condition.



1. simple if statement : 	

syntax : 

if condition:
    statement


example : 


age = 20
if age >= 18:
    print("Eligible to vote")




2.  if else statement : 

syntax : 

if condition1:
    statement1
else:
    statement2


example : 


number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")





3. if-elif-else : 

syntax : 

 if condition1:
    statement1
elif condition2:
    statement2
elif condition3:
    statement3
else:
    statement4



example : 


marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")




4. nested if : 

syntax : 

if condition1:
    if condition2:
        statement1



example : 


age = 22
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")




5. nested if else : 

syntax :


if condition1:
    if condition2:
        statement1
    else:
        statement2
else:
    statement3


example : 

age = 20
has_id = False

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Entry denied")



6. nested if elif else : 

syntax : 

if condition1:
    if condition2:
        statement1
    elif condition3:
        statement2
    else:
        statement3
else:
    statement4

example : 


marks = 82

if marks >= 35:
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 60:
        print("Grade C")
    else:
        print("Pass")
else:
    print("Fail")

"""



# Write a program to create a simple calculator that accepts two numbers and an operator (+, -, *, /). Display an error for an invalid operator or division by zero.
# a = int(input("Enter the num: "))
# b = int(input("Enter the num: "))
# op = input("enter operator(+, -, *, /): ")

# if op == "+":
#     print(a + b)
# elif op == "-":
#     print(a - b)
# elif op == "-":
#     print(a * b)
# elif op == "*":
#     print(a * b)
# elif op == "/":
#     print(a / b)
#     if b != 0:
#         print(a / b)
#     else:
#         print("Number is not divisible by zero")
# else:
#     print("invalid credentials")


# Write a program to check whether a person is eligible for a loan based on age (at least 21) and monthly salary (at least ₹25,000).

# salary = int(input("Enter the salary: "))
# age = int(input("Enter the age: "))

# if age >= 21 and age <120 and salary > 25000:
#     print("person is eligible for loan")
# else:
#     print("Person is not eligible for the loan")


# Write a program to determine whether a student is eligible to sit for an exam if attendance is at least 75% and fees are paid.

# attendence = int(input("Enter the attendence: "))
# fees_paid = input("Are fees paid? (yes/no): ")

# if attendence >= 75 and attendence <= 100 and fees_paid == "yes":
#     print("student is eligible to sit in the exam")
# else :
#     print("student is not eligible to sit in exam")


# Write a program to check whether a login is successful using a predefined username and password.

# username = "admin123"
# password = "admin@123"

# if username == "admin123" and password == "admin@123":
#     print("Login successful....!")
# else:
#     print("Login Failed....!")


# Write a program for an ATM withdrawal. Check whether the PIN is correct, the withdrawal amount is positive, the amount is a multiple of ₹100, and sufficient balance is available.

# password = int(input("Enter the pass: "))
# amount = int(input("Enter the amount: "))
# balance = 10000

# if password != 1234:
#     print("Incorrect Pass.....!")
# elif amount <= 0:
#     print("Invalid amount.....!")
# elif amount % 100 != 0:
#     print("Amount should be multiple of 100")
# elif amount > balance:
#     print("Low balance")
# else:
#     balance = balance - amount
#     print("Withdrawl Successful")
#     print(f"remaining balance {balance}")


# Write a program to determine the ticket price based on age:
# age = int(input("Enter the age: "))
# if age < 0 or age > 120:
#     print("Invalid age....!")
# elif age < 5 :
#     print("Ticket is free")
# elif age < 17:
#     print("Ticket price Should be 100")
# elif age < 59:
#     print("Ticket price should be 200")
# else:
#     print("Ticket price should be 120")


# Write a program to check whether a number is even or odd
# num = int(input("Enter the number: "))

# if num <= 0:
#     print("Invalid input....!")
# elif num % 2 == 0:
#     print(f"{num} is even number")
# else :
#     print(f"{num} odd number")


# Write a program to check whether a number is positive or non-positive.
# num = int(input("Enter the number: "))

# if num < 0:
#     print(f"{num} is negative number")
# else:
#     print(f"{num} is positive number") 


# Write a program to check voting eligibility using if-else
# age = int(input("Enter the age of the person: "))

# if age <= 0 or age > 120:
#     print("Invalid Age.....!")
# elif age >= 18:
#     print(f"{age} is verified & Person is eligible to vote")
# else:
#     print(" Person is not eligible to vote")

#  Write a program to check whether a number is divisible by both 3 and 5.
# num = int(input("Enter the number: "))

# if num % 3 == 0 and num % 5 == 0:
#     print(f"{num} is divisible by both 3 & 5")
# else:
#     print(f"{num} is not divisible")


# Write a program to check whether two numbers are equal or different.
# num = int(input("Enter the num: "))
# num2 = int(input("Enter the num: "))

# if num == num2 :
#     print(f"{num} & {num2} both are equal")
# else:
#     print(f"{num} & {num2} both are not equal")


# Take three numbers as input from the user
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))


# #  Write a program to find the greatest of three numbers
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))

# if (num1 >= num2) and (num1 >= num3):
#     greatest_num = num1
# elif (num2 >= num1) and (num2 >= num3):
#     greatest_num = num2
# else:
#     greatest_numt = num3


# print(f"The greatest number is: {greatest_num}")


# Write a program to classify a character as an uppercase letter, lowercase letter, digit, or special character
# char = input("Enter the character: ")

# if (char.isupper()):
#     print(f"{char} is uppercase")
# if (char.islower()):
#     print(f"{char} is lowercase")
# elif (char.isnumeric()):
#     print(f"{char} is digit")
# else:
#     print(f"{char} is special character")


# Write a program to check whether a number is positive; if positive, check whether it is even or odd
# num = int(input("Enter the num: "))

# if num > 0:
#     print(f"{num} is positive number")
#     if num % 2 == 0:
#         print(f"{num} is even number")
#     else:
#         print(f"{num} is odd number")
# else:
#     print(f"{num} is invalid number")


# Write a program to find the greatest of four numbers.
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))
# d = float(input("Enter fourth number: "))

# if a >= b and a >= c and a >= d:
#     greatest = a
# elif b >= a and b >= c and b >= d:
#     greatest = b
# elif c >= a and c >= b and c >= d:
#     greatest = c
# else:
#     greatest = d

# print(f"{greatest} is the greatest number among 4 numbers")
   

# Write a program to calculate an electricity bill using these slabs: first 100 units at ■2/unit, next 100 units at
# ■3/unit, and units above 200 at ■5/unit. Apply each rate only to the units in that slab.
# units = float(input("Enter the number of units: "))

# if units < 0:
#     print("Units can not be negative")
# elif units <= 100:
#     bill = units * 2
#     print(f"{bill} is the electricity bill")
# elif units <= 200:
#     bill = (100 * 2) + ((units - 100)*3)
#     print(f"{bill} is the electricity bill")
# else:
#     units <= 300
#     bill = (100*2)(100*3)((units - 200)*5)
#     print(f"{bill} is the electricity bill")


#  Write a program to calculate an employee bonus based on years of service: 10 or more years = 15%, 5–9
# years = 10%, fewer than 5 years = 5%.
# years = float(input("Years of service: "))
# salary = float(input("Enter the salary: "))

# if years < 0:
#     print("years cannot be negative")
# elif years >= 10:
#     Bonus = salary * 0.15
#     print(f"{Bonus} is the bonus for the service over 10 years")
# elif years >= 5:
#     Bonus = salary * 0.10
#     print(f"{Bonus} is the bonus for service over 5 years")
# else:
#     Bonus = salary * 0.5
#     print(f"{Bonus} is the bonus above 5 years of service")