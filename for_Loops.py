"""
for_loops :
     A for loop in Python is a programming tool used to repeat a block of code by stepping through a sequence of items one by one.
     Instead of repeating code manually, a for loop automatically grabs the first item, runs your instructions on it, moves to the second item, and repeats the process until it reaches the end of the sequence

     syntax:
         for item in iterable:
             # code block to execute
"""

# 1. Print numbers from 1 to 10.
# for i in range(1,11):
#     print(i)


# 2. Print numbers from 10 to 1 in reverse order.
# for i in range(10,0,-1):
#     print(i)


#3.  Print all even numbers between 1 and 50.
# for i in range(0,51):
#     if i % 2 == 0:
#         print(i)


# 4. Print all odd numbers between 1 and 50.
# for i in range(1,51):
#     if i % 2 != 0:
#         print(i)


#5.  Print the multiplication table of 5.
# for i in range(1, 11):
#     print(i*5)


# 6. Print the squares of numbers from 1 to 10.
# for i in range(1, 11):
#     print(i ** 2)


# 7. Print the cubes of numbers from 1 to 10.
# for i in range(1, 11):
#     print(i ** 3)


# 8. Print numbers from 1 to 100 that are divisible by 5.
# for i in range(1, 101):
#       if i % 5 == 0:
#             print(i)


# 9. Print the first 20 natural numbers and their corresponding squares.
# for i in range(1, 21):
#     print(f"Number: {i}, square :{i ** 2}")


# 10. Print the word 'Python' 10 times using a loop.
# for i in range(1, 11):
#     print("Python")    


"""11. Calculate the sum of numbers from 1 to 100.
method-2:-
total = sum(range(1, 101))
print(f"the sum of numbers from 1 to 100 is {total}")
method-1:-
total = 0
for i in range(1, 101):
     total += i
print(total)
 """


#12.  Calculate the sum of all even numbers between 1 and 100.
# total_sum = sum(range(2, 101, 2))
# print(total_sum)


# 13. Calculate the sum of all odd numbers between 1 and 100
# total_sum = sum(range(1, 101, 3))
# print(total_sum)


# 14.  Take a number from the user and print its multiplication table.
# num = int(input("Enter the number: "))
# for i in range(1, 11):
#     print(num * i)


# 15. Take a number from the user and calculate its factorial using a for loop.
# num = int(input("Enter the number: "))
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
# print(fact)


# 16. Count how many numbers between 1 and 100 are divisible by both 3 and 5.
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)


# 17. Find the sum of the digits of a positive integer using a for loop.
# num = 12345
# total_sum = 0

# for digit in str(num):
#     total_sum += int(digit)
# print(total_sum)


#18.  Count the number of digits in a positive integer using a for loop.
# num = 67895
# count = 0
# for _ in str(num):
#     count += 1
# print(count)


# 19. Print a square pattern of 5 rows and 5 columns using stars.
# Set the number of rows and columns
# size = 5

# for i in range(size):
    
#     for j in range(size):
       
#         print("*", end=" ")
    
#     print()


# 20. Count the vowels in a string using a for loop.
# vowels = "aeiou"
# count = 0
# for char in str(vowels):
#     count += 1
# print(count)


