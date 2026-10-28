"""
Collective Data Types :
    Collective types can hold multiple values or represent a collection of elements.
    ex --> 
    list, tuple, range, dict, set, frozenset   

1] Lists :
    A list is a built-in collection datatype used to store multiple values in a single variable.
    - A list stores multiple values.
    - A list is written using square brackets [].
    - Items are separated by commas.
    - A list can contain different datatypes.
    - A list is mutable, meaning we can modify its elements.
    - Lists allow duplicate values.
    - Lists maintain insertion order.
    ex --->
     students = ["Rahul", "Priya", "Amit", "Sneha", "Rohit"]
        print(students)
"""


# numbers = [10, 20, 30, 40, 50]
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])



# numbers = [10, 20, 30, 40, 50]
# print(numbers[-1])
# print(numbers[-2])
# print(numbers[-5])



# numbers = [10, 20, 30, 40, 50, 60]
# print(numbers[1:4])
# print(numbers[:3])
# print(numbers[3:])
# print(numbers[::-1])



# numbers = [10, 20, 30, 40]
# numbers[1] = 200
# print(numbers)



# inbuild python provided some functions like as : 
# marks = [78, 85, 92, 67, 88]
# print(len(marks))
# print(min(marks))
# print(max(marks))
# print(sum(marks))



# a = [14, 18, 24, 36]
# i= 0
# while i < (len(a)):
#     print(a[i])
#     i += 1



x = [15, 21, 39, 45, 67, 89, 97, 39]

# x.append(12) ----> add element at the end of list
# print(x)

# x.insert(1, 14) ----> adds element to the specific index by without deleting and shifting other numbers
# print(x)

# x.extend([112, 129, 135]) ----> Add multiple elements from an iterable
# print(x)

# x.remove(39) ----> used to remove defined element from the list
# print(x)   

# x.pop(-2) ----> removes thee element assign with the specific index
# print(x)

# x.clear() ----> Removes all element from the list
# print(x)

# print(x.index(39)) ----> Find the first matching element of the value

# print(x.count(39)) ----> Count occurrences of a value

# x.sort() ----> sort the list in place
# print(x)

# x.reverse() ----> reverse the list at the place
# print(x)

# new_x = x.copy() ---> create the copy of the existing list
# print(new_x)

