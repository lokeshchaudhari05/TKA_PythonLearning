"""
While Loops:
     A while loop in Python repeatedly executes a block of code as long as a specified boolean condition remains True.
     It is typically used when you do not know in advance how many times the loop needs to run.
     It consist three parts as:
         1.Initialization
         2.Condition 
         3.Updation ----> If not declared the loop will become infinite loop
     Syntax :
         while condition:
             //LOC
"""


# Print numbers from 1 to 10 using a while loop.
# i = 1
# while i <= 10:
#     print(i)
#     i += 1


# Print numbers from 10 to 1 in reverse order.
# i = 10 
# while i >= 1:
#     print(i)
#     i -= 1


# Print all even numbers between 1 and 50.
# i = 0
# while i <= 50:
#     print(i)
#     i += 2


# Print all odd numbers between 1 and 50.
# i = 1
# while i <= 50:
#     print(i)
#     i += 2


# Print the multiplication table of a number entered by the user.
# num = int(input("Enter the number: "))
# i = 1
# while i <= 10:
#     print(num * i)
#     i += 1
    

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# index = 0
# while index < len(nums):
#     print(nums[index])
#     index += 1


# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# i = 0
# while i < len(nums):
#     print(nums[i])
#     i += 1


nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i = 0
x = 36
while i < len(nums):
    if nums[i] == x:
        print(f"Found at index {i}")
        break
    else:
        print("Finding")
    i += 1