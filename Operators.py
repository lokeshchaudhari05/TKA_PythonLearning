"""  
1]Arithmetic Operators :-
     print(a + b) --->   Addition 
     print(a - b) --->   Subtraction
     print(a * b) --->   Multiplication 
     print(a / b) --->   Division (always gives the float value, even when the answer is whole i.e 5.0, return Quotient)
     print(a // b)--->   Floor Division (Gives only the whole part of the division)
     print(a % b) --->   modulus (Gives the remainder)
     print(a ** b)--->   exponentiation/power (means "to the power of")


a = int(input("Enter the value of a:- "))
b = int(input("Enter the value of b:- "))

print(a * b)
print(a - b)


Area of ractangle
#length = 15
#width = 8
#Area = length * width
#print("Area of Rectangle is", Area)



chocolates = 57
students = 6
print(chocolates / students)
print(chocolates % students)



a = int(input("Enter the number:- "))
print(a**2)
print(a**3)



total_minutes = 135
hours = total_minutes // 60
remaining_minutes = total_minutes % 60
print(total_minutes,"minutes equal to",hours,"hours and",remaining_minutes,"minutes")




num1 = 15
num2 = 18
num3 = 21
average = num1 + num2 + num3 / 3
print("The average is:", average)
"""


"""
2] Comparison operators:
      print(a == b) ---> Equal to
      print(a =! b) ---> Not equal to
      print(a > b) ----> Greater than
      print(a >= b) ---> Greater than or Equal to
      print(a < b) ----> Less than
      print(a <= b) ---> Less than or Equal to
"""



""""
3] Logical Operators:
      And : both values should be true
      Or  : atleast one value should be true
      Not : Flips true to false and vice-versa 

      
print(not True and 31 > 34 or not (32 > 21 and True) and not (True or 561-0))
print(not(0) and 34 > 34 or not (32 > 21 and not False) and not (False or 10))
print(("Ram" "ram") and (8 > 0) and (341 > 34) or not (32 > 21 and not True) and not (True or 56 - 10))
print(not False and (341 > 34) or not (int("32") >= 21 and not True) and not (True or 8.1 < 10))
print(not False and (34 < 50) or not (32 >= 21 and not ("Sahil" == "Sahil")) and not (True or 56 + (1-8)))
"""